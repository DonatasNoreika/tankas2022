from tankas import Tankas

tankas = Tankas()

tankas._generuoti_priesa()
tankas.info()
while True:
    if tankas.ar_ne_pabaiga():
        break
    print("\nPasirinkite: ")
    pasirinkimas = input("Judėti į \ns - šiaurę\np - pietus\nv - vakarus\nr - rytus\nx - iššauti\ni = informacija\nb - baigti žaidimą\n")
    if pasirinkimas == "s":
        tankas.siaure()
    if pasirinkimas == "p":
        tankas.pietus()
    if pasirinkimas == "v":
        tankas.vakarai()
    if pasirinkimas == "r":
        tankas.rytai()
    if pasirinkimas == "x":
        tankas.sauti()
    if pasirinkimas == "i":
        tankas.info()
    if pasirinkimas == "b":
        break