from random import randint

class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Š"
        self.suviai = [0, 0, 0, 0]
        self.priesas_x = 0
        self.priesas_y = 0
        self.taskai = 100
        self.priesai = 0

    def ar_ne_pabaiga(self):
        if self.taskai <= 0:
            print("\nŽaidimo pabaiga")
            print(f"Nukauta priešų: {self.priesai}")
            print(f"Šūviai: {self.suviai}, viso: {sum(self.suviai)}")
            return True
        return False


    def info(self):
        print(f"Taškai: {self.taskai}, nukauta priešų: {self.priesai}")
        print(f"Šūviai: {self.suviai}, viso: {sum(self.suviai)}")
        print(f"Koordinatės: X: {self.x}, Y: {self.y}, kryptis: {self.kryptis}")
        print(f"Priešas: X: {self.priesas_x}, Y: {self.priesas_y}")

    def _generuoti_priesa(self):
        self.priesas_x = randint(-10, 10)
        self.priesas_y = randint(-10, 10)

    def siaure(self):
        self.y += 1
        self.kryptis = "Š"
        self.taskai -= 10
        self.info()

    def pietus(self):
        self.y -= 1
        self.kryptis = "P"
        self.taskai -= 10
        self.info()

    def vakarai(self):
        self.x -= 1
        self.kryptis = "V"
        self.taskai -= 10
        self.info()

    def rytai(self):
        self.x += 1
        self.kryptis = "R"
        self.taskai -= 10
        self.info()

    def sauti(self):
        if self.kryptis == "Š":
            self.suviai[0] += 1
        if self.kryptis == "P":
            self.suviai[1] += 1
        if self.kryptis == "V":
            self.suviai[2] += 1
        if self.kryptis == "R":
            self.suviai[3] += 1
        if self._tikrinti_suvi():
            print("Priešas nukaltas!\n")
            self.priesai += 1
            self.taskai += 50
            self._generuoti_priesa()
        else:
            print("Nepataikei!\n")
        self.info()

    def _tikrinti_suvi(self):
        if self.x == self.priesas_x and self.y < self.priesas_y and self.kryptis == "Š":
            return True
        if self.x == self.priesas_x and self.y > self.priesas_y and self.kryptis == "P":
            return True
        if self.y == self.priesas_y and self.x < self.priesas_x and self.kryptis == "R":
            return True
        if self.y == self.priesas_y and self.x > self.priesas_x and self.kryptis == "V":
            return True
        return False


