from tankas import Tankas

tankas = Tankas()

tankas.generuoti_priesa()
tankas.info()
while True:
    print("Pasirinkite: ")
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