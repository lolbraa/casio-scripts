# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:47:56 2024

@author: sonog / Sondre

# TODO:
- La brukeren bestemme hvor mange resistanser man skal ha i parallell.
- Implementere flere serier.
- Optimalisering: Legge inn en automatisk nedre grense for potenser man sjekker. Man trenger ikke å sjekke 10ohm når man skal finne 500ohm.
- Optimalisering: Legge inn en sjekk for om den ønskede verdien er en perfekt E12 verdi. Hvis den er det, trenger man ikke dette skriptet, lol.

"""

def regnParallell():
    n = int(input("Hvor mange resistorer\nskal du ha i parallell? "))
    for i in range(n):
        R = float(input("R" + str(i+1) + " = "))
        if i == 0:
            Rsist = R
        else:
            Rsist = Rsist * R / (Rsist + R)
    print("\n", round(Rsist,3), "ohm i parallell.")

def finnOptimalParallell():
    R =  float(input("Hvilken resistans\nonsker du? "))# hvilke verdi jeg vil ha

    #input("Hvilken serie?")
    R12 = [10,12,15,18,22,27,33,39,47,56,68,82]

    # Hvor stor potens av E12 serien skal vi ga opp til?
    #iterasjoner = int(input("\nMaks verdi i E12.\nAnb. 10 for >1Mohm\n10^"))
    iterasjoner = len(str(round(R))) + 3
    #print(iterasjoner)

    Px = 1
    Py = 1

    R1 = 0
    R2 = 0
    RO = 0
    Rsist = 0
    R1sist = 0
    R2sist = 0

    feil = R**2
    Rny = 0

    for x in range(iterasjoner):
        Px = Px * 10
        Py = 1
        for y in range(iterasjoner):
            Py = Py * 10
            for i in range(12):
                for n in range(12):
                    R1 = Px * R12[i]
                    R2 = Py * R12[n]
                    RO = R1 * R2 / (R1 + R2)
                    if (RO - R)**2 < feil:  
                        feil = (RO - R)**2
                        Rsist = RO
                        R1sist = R1
                        R2sist = R2
    print("\n", round(Rsist,2),"ohm lages med\n", R1sist, "||", R2sist,"ohm.\nFeil med", round(((Rsist - R)**2)**(1/2),1), "ohm\n(" , round(100 * ((Rsist - R)**2)**(1/2) / R,4), "% feil)")               

# Kjører i loop for å regne flere resistanser etter hverandre
while True:
    if input("Regn parallell (0) eller\nfinn optimal E12 (1)\n(0/1)") == "0":
        regnParallell()
    else:
        finnOptimalParallell()

    #print("\n\n")
    if input("Avslutt (0) eller\nfortsett (1)\n(0/1)") == "0":
        break
    else:
        continue