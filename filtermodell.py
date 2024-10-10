import math

def acosh(x):
    return math.log(x + math.sqrt(x * x - 1))

def cosh(x):
    return (math.exp(x) + math.exp(-x)) / 2


def finnApproksimasjon():
    print("Dette programmet gir deg\nverdiene til ulike\nfilterapproksimasjoner.")
    while True:
        print("Velg filtertype:")
        passType = input("LP eller HP? (1/2): ").strip().upper()
        if passType in ['1', '2']:
            break
        else:
            print("Ugyldig valg.\nVelg 'B' for Butterworth\neller 'C' for Chebyshev.")

    while True:
        print("Velg approksimasjonsmodell:")
        approksimasjonsType = input("Butt. eller Cheb.? (1/2): ").strip().upper()
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




finnApproksimasjon()




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
