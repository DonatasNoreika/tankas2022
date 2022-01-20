class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Š"
        self.suviai = []

    def _koordinates(self):
        print(f"Koordinatės: X: {self.x}, Y: {self.y}, kryptis: {self.kryptis}")

    def siaure(self):
        self.y += 1
        self.kryptis = "Š"
        self._koordinates()

    def pietus(self):
        self.y -= 1
        self.kryptis = "P"
        self._koordinates()

    def vakarai(self):
        self.x -= 1
        self.kryptis = "V"
        self._koordinates()

    def rytai(self):
        self.x += 1
        self.kryptis = "R"
        self._koordinates()

