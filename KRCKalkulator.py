# Kristoffer Braa og GitHub Copilot
# 10.10.2024

# INFORMASJON OM KALKULATOREN:
# Når man er i editor vil Shift + 4 vise alle kommandoer som er mulige i micropython-implementasjonen
# Begrensninger i kalkulatoren er mange:
#   - Den kan kun vise 21 tegn per linje.
#   - Den kan kun vise 5 linjer, og det er ikke mulig å bla (?)
#   - Den mangler mange python bibliotek, og implementasjonene av feks math er mangelfulle (mangler acosh og cosh)
#   - Det er ikke mulig å formatere teksten, altså ingen farger og ikke mulig å bruke print(f"")
#   - Støtter ikke æ, ø, å og mange andre utvidede ascii-tegn


# INSTRUKS FOR EMULERING AV CASIO fx-CG50:
# Emulator (Windows og Mac) kan lastes ned herifra https://education.casio.co.uk/emulator/download-emulator-software/.
# Når du installerer, ikke velg lisens-greier. 
# For å laste fila over i kalkulatoren, gå til Memory i menyen -> Import/Export -> Import files og velg fila du skal importere.

# INSTRUKS FOR BRUK PÅ CASIO fx-CG50:
# 1. Koble kalkulatoren til PCen med USB 2.0 type A til mini-B kabel. [bilde](https://www.bhphotovideo.com/images/images1000x1000/kramer_c_usb_mini5_10_usb_2_0_a_m_to_1471735.jpg)
# 2a. Hvis du får opp en dialogboks på kalkulatoren, velg "USB Flash [F1]".
# 2b. Hvis du ikke får opp dialogboksen, trykk MENU -> Link -> RECV [F2].
# 3. Kalkulatoren skal dukke opp som en minnepenn. Overfør fila til kalkulatoren, feks til root-folderen eller @MainMem.  
# 4. VIKTIG: Kalkulatoren sier selv at det er ekstremt viktig å "unmounte" kalkulatoren før du tar ut USB-kabelen. På PCen, høyreklikk på kalkulatoren og velg "Eject" eller likenende. Windows har et ikon på taskbaren.
# 5. Når kalkulatoren er ejected, følg instruksene på skjermen og gå til Python i menyen.abs
# 6. Finn filen og kjør den med EXE-knappen eller F1.
# Si ifra hvis noe ikke fungerer som forventet


# TODO:
# - 1. ordens KRC-filter, blant annet for feks. 3. ordens filtre
#   - finnKRC_LP_1ordens() er ikke implementert
#   - finnKRC_HP_1ordens() er ikke implementert
# - Båndpassfilter
#   - finnKRC_BP(i) er ikke implementert
# - Denomarlisering av (Omega0, Q)-tabeller 
# - Denomarlisering av pol-tabeller 
# - Oppslagg av resistansverdier basert på serier
# - Oppslagg av kondensatorverdier basert på serier
# - Oppslagg av resistansverdier som krever flere motstandere, i serie og paralell


import math

####################### HJELPEFUNKSJONER #######################

# Kalkulator har ikke acosh og cosh, sa vi definerer de selv
def acosh(x):
    return math.log(x + math.sqrt(x * x - 1))
def cosh(x):
    return (math.exp(x) + math.exp(-x)) / 2

####################### HOVEDFUNKSJONER #######################

def init():
    global modus, passType, verbosity
    # sporr hvilken handling brukeren vil utfore
    while True:
        print("\nVelg handling:")
        modus = input("1: Regn Approks.-modell\n2: Regn KRC-filter\n3: Forst 1 sa 2\n(1/2/3): ").strip()
        if modus in ['1', '2', '3']:
            break
        else:
            print("Ugyldig valg. Vennligst velg 1, 2 eller 3.")

    # spor om filtertype, lavpass eller hoypass (eller bandpass)
    while True:
        print("\nVelg filtertype:")
        passType = input("LP, HP eller Bandpass?\n(1/2/3): ")
        if passType in ['1', '2']:
            break
        else:
            print("Ugyldig valg.\nVelg '1' for Lavpass\neller '2' for Hoypass.\nbandpass ikke implementert.")

    # spor om filtertype, lavpass eller hoypass (eller bandpass)
    while True:
        print("\nHvor mye informasjon vil du ha?\n1: Kun nodvendig\n2: Alle mellomregninger")
        verbosity = input("Verbosity\n(1/2): ")
        if verbosity in ['1', '2']:
            break
        else:
            print("Ugyldig valg.")



def finnApproksimasjon(passType):
    print("\nDette programmet gir deg\nverdiene til ulike\nfilterapproksimasjoner.")
    global n

    # spor om hvilken approksimasjonsmodell brukeren vil bruke
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

    if passType == '1': # regner selektiviteten basert pa om det er lavpass eller hoypass
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

    print("\nBruk disse verdiene til a finne riktig verdier i tabellen.")



def finnKRC(passType):
    print("\nFinn verdier for et\nKRC-filter/Sallen-Key\n-filter. OBS:\nIngen forsterkning, k.")
    
    # spor etter orden n
    while True:
        try:
            n = int(input("\nSkriv inn\norden n: "))
            if n > 1:
                break
            else:
                print("Orden n ma vere et\nheltall storre enn 1.")
        except ValueError:
            print("Ugyldig input.\nVennligst skriv inn\net heltall.")

    if passType == '1': # Lavpass
        print("\nBeregner lavpass-krets\n av orden ", n, ".")
        for i in range(1, int(n/2) + 1):
            print("\nRegn ut T", i)
            finnKRC_LP_2ordens(i)

        if n % 2 == 1: # hvis n er oddetall, ma vi regne ut en ekstra 1. ordens
            print("Regn ut 1. ordens T", n)
            finnKRC_LP_1ordens()
        

    elif passType == '2': # Hoypass
        print("\nBeregner hoypass-\nkrets av orden", n)
        print("Bruker C = C1 = C2 og\nC er like i alle trinn.")
        C = float(input("Oppgi onsket C i pF\n(10^-12): ")) * (10 ** -12)
        for i in range(1, int(n/2) + 1):
            print("\nRegn ut T", i)
            finnKRC_HP_2ordens(C,i)

        if n % 2 == 1: # hvis n er oddetall, ma vi regne ut en ekstra 1. ordens
            print("Regn ut 1. ordens T", n)
            finnKRC_HP_1ordens()


    elif passType == '3': # Bandpass
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
    R = float(input("Velg R i \nohm: "))
    
    C2_temp = 1 / (2 * R * w0 * Q)
    print("\nC2_temp: ", C2_temp)
    
    C2 = float(input("Oppgi onsket C2 i\npF (10^-12): ")) * (10 ** -12)
    C1_temp = 4 * (Q ** 2) * C2
    print("\nC1_temp: ", C1_temp)
    
    C1 = float(input("Oppgi onsket C1 i\npF (10^-12): "))* (10 ** -12)
    n = C1 / C2
    k = n / (2 * (Q ** 2)) - 1
    m = k + math.sqrt((k ** 2) - 1)
    R2 = 1 / (math.sqrt(m * n) * w0 * C2)
    R1 = m * R2
    
    print("\nR1: ", R1)
    print("R2: ", R2)

    # hvis hoyere verbosity, skriv ut alle variabler
    if verbosity == '2':
        print("w0: ", w0)
        print("Q: ", Q)
        input("<enter> for neste")
        print("R: ", R)
        print("C2: ", C2)
        print("C1: ", C1)
        print("n: ", n)
        input("<enter> for neste")
        print("k: ", k)
        print("m: ", m)

    print("w0_reell: ", 1 / (sqrt(R1 * R2) * C))
    print("Q_reell: ", sqrt(R1 * R2) / 2)
    input("<enter> for neste")


def finnKRC_LP_1ordens():
    print("Funksjonen ikke implementert")


def finnKRC_HP_2ordens(C, i):
    w0 = float(input("Skriv inn w0 i\nrad/s: "))
    Q = float(input("Skriv inn Q: "))
    
    R1_temp = 1 / (2 * Q * w0 * C)
    print("\nR1_temp: ", R1_temp)
    R1 = float(input("Oppgi onsket R1 i\nohm: "))

    R2_temp = (2 * Q) / (w0 * C)
    print("\nR2_temp: ", R2_temp)
    R2 = float(input("Oppgi onsket R2 i\nohm: "))
    
    print("\nR1: ", R1)
    print("R2: ", R2)

    # hvis hoyere verbosity, skriv ut alle variabler
    if verbosity == '2':
        print("w0: ", w0)
        print("Q: ", Q)
        input("<enter> for neste")
        print("C: ", C)
        print("R1: ", R1)
        print("R2: ", R2)
    print("w0_reell: ", 1 / (math.sqrt(R1 * R2) * C))
    print("Q_reell: ", math.sqrt(R1 / R2) / 2)
    input("<enter> for neste")


def finnKRC_HP_1ordens():
    print("Funksjonen er ikke implementert enna.")


def finnKRC_BP(i):
    print("Funksjonen er ikke implementert enna.")

####################### MAIN #######################

def main():
    init()
    if modus == '1':
        finnApproksimasjon(passType)
    elif modus == '2':
        finnKRC(passType)
    elif modus == '3':
        finnApproksimasjon(passType)
        print("\nDet er ikke implementert\noverføring av verdier")
        finnKRC(passType)

main()



# Takk Copilot
""" 
Lag et micropython-skript som folger disse stegene:

Sporr om brukeren skal lage butterworth eller chebyshev
Sporre brukeren om fp, fs, Dripple, Ds

Hvis Butterworth, gjor folgende:
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
 Hvis lavpass, gjor folgende:

Fa fra bruker w0, Q, og R

Regn ut

C2_temp = 1 / (2 * R * w0 * Q)
Be bruker oppgi C2 han onsker i pF (10 ^ -12)
Regn ut C1_temp = 4 * Q ^2 * C2
Be bruker oppgi C1
n = C1 / C2
k = n / (2 * Q ^2) - 1
m = k + sqrt(k ^2 - 1)
R2 = 1 / (sqrt(m*n) * w0 * C2)
R1 = m * R2
  """
