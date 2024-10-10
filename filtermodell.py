import math

def acosh(x):
    return math.log(x + math.sqrt(x * x - 1))

def cosh(x):
    return (math.exp(x) + math.exp(-x)) / 2


def finnApproksimasjon(passType):
    print("Dette programmet gir deg\nverdiene til ulike\nfilterapproksimasjoner.")

    while True:
        print("Velg approksimasjonsmodell:")
        approksimasjonsType = input("Butt. eller Cheb.?\n(1/2): ").strip().upper()
        if approksimasjonsType in ['1', '2']:
            break
        else:
            print("Ugyldig valg.\nVelg 'B' for Butterworth\neller 'C' for Chebyshev.")

    fp = float(input("Skriv inn fp: "))
    fs = float(input("Skriv inn fs: "))
    Dripple = float(input("Skriv inn Dripple: "))
    Ds = float(input("Skriv inn Ds: "))

    if passType == '1':
        OmegaS = fs / fp
    else:
        OmegaS = fp / fs

    epsilon = math.sqrt(10 ** (Dripple / 10) - 1)


    if approksimasjonsType == '1':
        n = math.ceil((Ds - 20 * math.log(epsilon, 10)) / (20 * math.log(OmegaS, 10)))
        Omega3dB = ((10 ** 0.3 - 1) / (epsilon ** 2)) ** (1 / (2 * n))
        
        print("OmegaS: ", OmegaS)
        print("Epsilon: ", epsilon)
        print("Orden n: ", n)
        print("Omega3dB: ", Omega3dB)
    elif approksimasjonsType == '2':
        n = math.ceil(acosh(10 ** (Ds / 20) / epsilon) / acosh(OmegaS))
        Omega3dB = cosh((acosh( math.sqrt(10 ** 0.3 - 1) / epsilon)) / n)
        
        print("OmegaS: ", OmegaS)
        print("Epsilon: ", epsilon)
        print("Orden n: ", n)
        print("Omega3dB: ", Omega3dB)
    else:
        print("Ugyldig valg.\nVelg enten 'B' for Butterworth\neller 'C' for Chebyshev.")

    print("Bruk disse verdiene til å finne riktig verdier i tabellen.")


def finnKRC_LP():

    w0 = float(input("Skriv inn w0: "))
    Q = float(input("Skriv inn Q: "))
    R = float(input("Skriv inn R: "))
    
    C2_temp = 1 / (2 * R * w0 * Q)
    print("C2_temp: ", C2_temp)
    
    C2 = float(input("Oppgi ønsket C2 i pF (10^-12): ")) * 10 ** -12
    C1_temp = 4 * Q ** 2 * C2
    print("C1_temp: ", C1_temp)
    
    C1 = float(input("Oppgi ønsket C1: "))
    n = C1 / C2
    k = n / (2 * Q ** 2) - 1
    m = k + math.sqrt(k ** 2 - 1)
    R2 = 1 / (math.sqrt(m * n) * w0 * C2)
    R1 = m * R2
    
    print("R1: ", R1)
    print("R2: ", R2)

def finnKRC(passType):
    print("Finn verdier for et KRC-filter,\nogså kalt Sallen-Key-filter.\nOBS: Ingen forsterkning, K.")
    
    if passType == '1':
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
        finnKRC_LP()
    else:
        print("Ugyldig valg. Velg '1' for LP.")



def main():
    # spørr hvilken handling brukeren vil utføre
    while True:
        print("Velg handling:")
        valg = input("1: Finn verdier for en approksimasjons-modell\n2: Finn verdier for et KRC-filter\n3: Først 1 så 2\n(1/2/3): ").strip()
        if valg in ['1', '2', '3']:
            break
        else:
            print("Ugyldig valg. Vennligst velg 1, 2 eller 3.")

    # spør om filtertype, lavpass eller høypass (eller båndpass)
    while True:
        print("Velg filtertype:")
        passType = input("LP eller HP?\n(1/2): ").strip().upper()
        if passType in ['1', '2']:
            break
        else:
            print("Ugyldig valg.\nVelg '1' for Lavpass\neller '2' for Høypass.")

    if valg == '1':
        finnApproksimasjon(passType)
    elif valg == '2':
        finnKRC(passType)
    elif valg == '3':
        finnApproksimasjon(passType)
        finnKRC(passType)

main()



""" Lag et micropython-skript som følger disse stegene:

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
3. Regn ut Omega3dB = cosh( (acosh( sqrt(10 ^ (0.3) - 1) / epsilon ) / n) ) """
