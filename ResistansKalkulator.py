# Skrevet av Sondre

R12 = [10,12,15,18,22,27,33,39,47,56,68,82]

R = 15775# hvilke verdi jeg vil ha

Px = 1
Py = 1

R1 = 0
R2 = 0
RO = 0

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
                    print(RO, R1, R2, round(((RO - R)**2)**(1/2),1), round(100 * ((RO - R)**2)**(1/2) / R,4))