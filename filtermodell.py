# Kristoffer Braa og GitHub Copilot
# 10.10.2024

import math

####################### HJELPEFUNKSJONER #######################

# Kalkulator har ikke acosh og cosh, så vi definerer de selv
def acosh(x):
    return math.log(x + math.sqrt(x * x - 1))
def cosh(x):
    return (math.exp(x) + math.exp(-x)) / 2

####################### HOVEDFUNKSJONER #######################

def init():
    global modus, passType, verbosity
    # spørr hvilken handling brukeren vil utføre
    while True:
        print("\nVelg handling:")
        modus = input("1: Finn verdier for en approksimasjons-modell\n2: Finn verdier for et KRC-filter\n3: Først 1 så 2\n(1/2/3): ").strip()
        if modus in ['1', '2', '3']:
            break
        else:
            print("Ugyldig valg. Vennligst velg 1, 2 eller 3.")

    # spør om filtertype, lavpass eller høypass (eller båndpass)
    while True:
        print("\nVelg filtertype:")
        passType = input("LP, HP eller Båndpass?\n(1/2/3): ")
        if passType in ['1', '2']:
            break
        else:
            print("Ugyldig valg.\nVelg '1' for Lavpass\neller '2' for Høypass.\nbåndpass ikke implementert.")

    # spør om filtertype, lavpass eller høypass (eller båndpass)
    while True:
        print("\nHvor mye informasjon vil du ha?\n1: Kun nødvendig\n2: Alle mellomregninger")
        verbosity = input("Verbosity\n(1/2): ")
        if verbosity in ['1', '2']:
            break
        else:
            print("Ugyldig valg.")



def finnApproksimasjon(passType):
    print("\nDette programmet gir deg\nverdiene til ulike\nfilterapproksimasjoner.")

    # spør om hvilken approksimasjonsmodell brukeren vil bruke
    while True:
        print("Velg approksimasjonsmodell:")
        approksimasjonsType = input("Butt. eller Cheb.?\n(1/2): ")
        if approksimasjonsType in ['1', '2']:
            break
        else:
            print("Ugyldig valg.\nVelg 'B' for Butterworth\neller 'C' for Chebyshev.")

    fp = float(input("\nSkriv inn fp: "))
    fs = float(input("Skriv inn fs: "))
    Dripple = float(input("Skriv inn Dripple: "))
    Ds = float(input("Skriv inn Ds: "))

    if passType == '1': # regner selektiviteten basert på om det er lavpass eller høypass
        OmegaS = fs / fp
    else:
        OmegaS = fp / fs

    epsilon = math.sqrt(10 ** (Dripple / 10) - 1)

    if approksimasjonsType == '1': # Butterworth
        n = math.ceil((Ds - 20 * math.log(epsilon, 10)) / (20 * math.log(OmegaS, 10)))
        Omega3dB = ((10 ** 0.3 - 1) / (epsilon ** 2)) ** (1 / (2 * n))
        
        print("OmegaS: ", OmegaS)
        print("Epsilon: ", epsilon)
        print("Orden n: ", n)
        print("Omega3dB: ", Omega3dB)
    elif approksimasjonsType == '2': # Chebyshev
        n = math.ceil(acosh(10 ** (Ds / 20) / epsilon) / acosh(OmegaS))
        Omega3dB = cosh((acosh( math.sqrt(10 ** 0.3 - 1) / epsilon)) / n)
        
        print("OmegaS: ", OmegaS)
        print("Epsilon: ", epsilon)
        print("Orden n: ", n)
        print("Omega3dB: ", Omega3dB)
    else:
        print("Ugyldig valg.")

    print("\nBruk disse verdiene til å finne riktig verdier i tabellen.")



def finnKRC(passType):
    print("\nFinn verdier for et KRC-filter,\nogså kalt Sallen-Key-filter.\nOBS: Ingen forsterkning, k.")
    
    # spør etter orden n
    while True:
        try:
            n = int(input("Skriv inn orden n: "))
            if n > 1:
                break
            else:
                print("Orden n må være et heltall større enn 1.")
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et heltall.")

    if passType == '1': # Lavpass
        print("\nBeregner lavpass-krets\n av orden ", n, ".")
        for i in range(1, int(n/2) + 1):
            print("\nRegn ut T", i)
            finnKRC_LP_2ordens(i)

        if n % 2 == 1: # hvis n er oddetall, må vi regne ut en ekstra 1. ordens
            print("Regn ut 1. ordens T", n)
            finnKRC_LP_1ordens()
        

    elif passType == '2': # Høypass
        print("\nBeregner høypass-krets\nav orden", n)
        print("Bruker C = C1 = C2,\nog at C og w0 er like i alle Tn.")
        C = float(input("Velg Ci pF (10^-12): ")) * (10 ** -12)
        w0 = float(input("Skriv inn w0\ni rad/s: "))
        for i in range(1, int(n/2) + 1):
            print("\nRegn ut T", i)
            finnKRC_HP_2ordens(C,i)

        if n % 2 == 1: # hvis n er oddetall, må vi regne ut en ekstra 1. ordens
            print("Regn ut 1. ordens T", n)
            finnKRC_HP_1ordens()


    elif passType == '3': # Båndpass
        print("\n")
        for i in range(1, n + 1):
            print("Regn ut T", i)
            finnKRC_BP(i)

    else:
        print("Ugyldig valg.")


####################### DETALJ-FUNKSJONER #######################

def finnKRC_LP_2ordens(i):
    w0 = float(input("Skriv inn w0\ni rad/s: "))
    Q = float(input("Skriv inn Q: "))
    R = float(input("Velg R\ni ohm(ikke kilo): "))
    
    C2_temp = 1 / (2 * R * w0 * Q)
    print("\nC2_temp: ", C2_temp)
    
    C2 = float(input("Oppgi ønsket C2\ni pF (10^-12): ")) * (10 ** -12)
    C1_temp = 4 * (Q ** 2) * C2
    print("\nC1_temp: ", C1_temp)
    
    C1 = float(input("Oppgi ønsket C1\ni pF (10^-12): "))* (10 ** -12)
    n = C1 / C2
    k = n / (2 * (Q ** 2)) - 1
    m = k + math.sqrt((k ** 2) - 1)
    R2 = 1 / (math.sqrt(m * n) * w0 * C2)
    R1 = m * R2
    
    print("\nR1: ", R1)
    print("R2: ", R2)

    # hvis høyere verbosity, skriv ut alle variabler
    if verbosity == '2':
        print("w0: ", w0)
        print("Q: ", Q)
        print("R: ", R)
        print("C2: ", C2)
        print("C1: ", C1)
        print("n: ", n)
        print("k: ", k)
        print("m: ", m)

    print("\nVERIFIKASJON: ")
    print("w0_reell: ", 1 / (sqrt(R1 * R2) * C))
    print("Q_reell: ", sqrt(R1 * R2) / 2)

def finnKRC_LP_1ordens():
    print("Funksjonen er ikke implementert ennå.")


def finnKRC_HP_2ordens(w0, C, i):
    Q = float(input("Skriv inn Q: "))
    
    R1_temp = 1 / (2 * Q * w0 * C)
    print("\nR1_temp: ", R1_temp)
    R1 = float(input("Oppgi ønsket R1\ni ohm: "))

    R2_temp = (2 * Q) / (w0 * C)
    print("\nR2_temp: ", R2_temp)
    R2 = float(input("Oppgi ønsket R2: "))
    
    print("\nR1: ", R1)
    print("R2: ", R2)

    # hvis høyere verbosity, skriv ut alle variabler
    if verbosity == '2':
        print("w0: ", w0)
        print("Q: ", Q)
        print("R1: ", R1)
        print("R2: ", R2)
        print("C: ", C)
    
    print("\nVERIFIKASJON: ")
    print("w0_reell: ", 1 / (math.sqrt(R1 * R2) * C))
    print("Q_reell: ", math.sqrt(R1 / R2) / 2)


def finnKRC_HP_1ordens():
    print("Funksjonen er ikke implementert ennå.")


def finnKRC_BP(i):
    print("Funksjonen er ikke implementert ennå.")

####################### MAIN #######################

def main():
    init()
    if modus == '1':
        finnApproksimasjon(passType)
    elif modus == '2':
        finnKRC(passType)
    elif modus == '3':
        finnApproksimasjon(passType)
        finnKRC(passType)

main()



# Takk Copilot
""" 
Lag et micropython-skript som følger disse stegene:

Spørr om brukeren skal lage butterworth eller chebyshev
Spørre brukeren om fp, fs, Dripple, Ds

Hvis Butterworth, gjør følgende:
Regn ut OmegaS = fs/fp
Regn ut epsilon = sqrt(10 ^(Dripple / 10) -1 )
Regn ut n = (Ds - 20 * log(epsilon) / (20*log(OmegaS)), og regn opp til nærmeste heltall.
Regn ut Omega3dB = ((10⁽0.3) - 1) / (epsilon ^2)) ^ (1 / (2*pi)


implementer chebyshev
1. Regn ut epsilon = sqrt(10 ^(Dripple / 10) -1 )
2. n = (acosh( (10 ^ (Ds / 20) / epsilon) )) / (acosh(OmegaS)) ) og regn opp til nærmeste heltall
3. Regn ut Omega3dB = cosh( (acosh( sqrt(10 ^ (0.3) - 1) / epsilon ) / n) ) 
"""

""" 
On my casio fx cg50 this thros an syntax error when using micropython
 """


""" 
implementer chebyshev

Regn ut epsilon = sqrt(10 ^(Dripple / 10) -1 )
n = (acosh( (10 ^ (Ds / 20) / epsilon) )) / (acosh(OmegaS)) ) og regn opp til nærmeste heltall
Regn ut Omega3dB = cosh( (acosh( sqrt(10 ^ (0.3) - 1) / epsilon ) / n) )
 """

 """ cg50 gives error "no attribute acosh" """


 """ 
 Hvis lavpass, gjør følgende:

Få fra bruker w0, Q, og R

Regn ut

C2_temp = 1 / (2 * R * w0 * Q)
Be bruker oppgi C2 han ønsker i pF (10 ^ -12)
Regn ut C1_temp = 4 * Q ^2 * C2
Be bruker oppgi C1
n = C1 / C2
k = n / (2 * Q ^2) - 1
m = k + sqrt(k ^2 - 1)
R2 = 1 / (sqrt(m*n) * w0 * C2)
R1 = m * R2
  """
