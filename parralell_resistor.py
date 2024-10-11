# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:47:56 2024

@author: sonog
"""
R =  15775# hvilke verdi jeg vil ha

R12 = [10,12,15,18,22,27,33,39,47,56,68,82]

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

for x in range(9):
    Px = Px * 10
    Py = 1
    for y in range(9):
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
print(round(Rsist,2),"Ω <- ", R1sist, "Ω  ||", R2sist,"Ω. og feil med", round(((Rsist - R)**2)**(1/2),1), "Ω = " , round(100 * ((Rsist - R)**2)**(1/2) / R,4), "% feil")               
        