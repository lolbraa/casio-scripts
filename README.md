Dette er en repo for casio-skripts for elektro

# INFORMASJON OM KALKULATOREN:
 Når man er i editor vil Shift + 4 vise alle kommandoer som er mulige i micropython-implementasjonen
 Begrensninger i kalkulatoren er mange:
   - Den kan kun vise 21 tegn per linje.
   - Den kan kun vise 5 linjer, og det er ikke mulig å bla (?)
   - Den mangler mange python bibliotek, og implementasjonene av feks math er mangelfulle (mangler acosh og cosh)
   - Det er ikke mulig å formatere teksten, altså ingen farger og ikke mulig å bruke print(f"")
 
 # INSTRUKS FOR EMULERING AV CASIO fx-CG50:
 Emulator (Windows og Mac) kan lastes ned herifra https://education.casio.co.uk/emulator/download-emulator-software/.
 Når du installerer, ikke velg lisens-greier. 
 For å laste fila over i kalkulatoren, gå til Memory i menyen -> Import/Export -> Import files og velg fila du skal importere.
 
 # INSTRUKS FOR BRUK PÅ CASIO fx-CG50:
 1. Koble kalkulatoren til PCen med USB 2.0 type A til mini-B kabel. ![bilde](https://www.bhphotovideo.com/images/images1000x1000/kramer_c_usb_mini5_10_usb_2_0_a_m_to_1471735.jpg)
 2. A: Hvis du får opp en dialogboks på kalkulatoren, velg "USB Flash [F1]". B: Hvis du ikke får opp dialogboksen, trykk MENU -> Link -> RECV [F2].
 4. Kalkulatoren skal dukke opp som en minnepenn. Overfør fila til kalkulatoren, feks til root-folderen eller @MainMem.  
 5. VIKTIG: Kalkulatoren sier selv at det er ekstremt viktig å "unmounte" kalkulatoren før du tar ut USB-kabelen. På PCen, høyreklikk på kalkulatoren og velg "Eject" eller likenende. Windows har et ikon på taskbaren.
 6. Når kalkulatoren er ejected, følg instruksene på skjermen og gå til Python i menyen.abs
 7. Finn filen og kjør den med EXE-knappen eller F1.
 Si ifra hvis noe ikke fungerer som forventet


# TODO:
 - 1. ordens KRC-filter, blant annet for feks. 3. ordens filtre
   - finnKRC_LP_1ordens() er ikke implementert
   - finnKRC_HP_1ordens() er ikke implementert
 - Båndpassfilter
   - finnKRC_BP(i) er ikke implementert
 - Denomarlisering av (Omega0, Q)-tabeller 
 - Denomarlisering av pol-tabeller 
 - Oppslagg av resistansverdier basert på serier
 - Oppslagg av kondensatorverdier basert på serier
 - Oppslagg av resistansverdier som krever flere motstandere, i serie og paralell