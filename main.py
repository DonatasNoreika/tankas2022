from tankas import Tankas

tankas = Tankas()

while True:
    print("Pasirinkite: ")
    pasirinkimas = input("Judėti į \ns - šiaurę\np - pietus\nv - vakarus\nr - rytus\nx - iššauti\n")
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