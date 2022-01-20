from tankas import Tankas

tankas = Tankas()

while True:
    print("Pasirinkite: ")
    pasirinkimas = input("Judėti į \nS - šiaurę\nP - pietus\nV - vakarus\nR - rytus\n")
    if pasirinkimas == "S":
        tankas.siaure()
    if pasirinkimas == "P":
        tankas.pietus()
    if pasirinkimas == "V":
        tankas.vakarai()
    if pasirinkimas == "R":
        tankas.rytai()