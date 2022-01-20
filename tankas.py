from random import randint

class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Š"
        self.suviai = [0, 0, 0, 0]
        self.priesas_x = 0
        self.priesas_y = 0

    def info(self):
        print(f"Koordinatės: X: {self.x}, Y: {self.y}, kryptis: {self.kryptis}")
        print(f"Šūviai: {self.suviai}, viso: {sum(self.suviai)}")
        print(f"Priešas: X: {self.priesas_x}, Y: {self.priesas_y}")

    def generuoti_priesa(self):
        self.priesas_x = randint(-10, 10)
        self.priesas_y = randint(-10, 10)

    def siaure(self):
        self.y += 1
        self.kryptis = "Š"
        self.info()

    def pietus(self):
        self.y -= 1
        self.kryptis = "P"
        self.info()

    def vakarai(self):
        self.x -= 1
        self.kryptis = "V"
        self.info()

    def rytai(self):
        self.x += 1
        self.kryptis = "R"
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
        self.info()
