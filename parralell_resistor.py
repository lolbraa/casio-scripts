# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:47:56 2024

@author: sonog
"""
R =  float(input("Hvilken resistans\nonsker du?"))# hvilke verdi jeg vil ha

#input("Hvilken serie?")
R12 = [10,12,15,18,22,27,33,39,47,56,68,82]

# Hvor stor potens av E12 serien skal vi ga opp til?
#iterasjoner = int(input("\nMaks verdi i E12.\nAnb. 10 for >1Mohm\n10^"))
iterasjoner = len(str(round(R))) + 3
print(iterasjoner)

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
print("\n", round(Rsist,2),"ohm\n", R1sist, "||", R2sist,"ohm.\nFeil med", round(((Rsist - R)**2)**(1/2),1), "ohm\n(" , round(100 * ((Rsist - R)**2)**(1/2) / R,4), "% feil)")               
        