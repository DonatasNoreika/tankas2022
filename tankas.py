class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Š"
        self.suviai = [0, 0, 0, 0]

    def _info(self):
        print(f"Koordinatės: X: {self.x}, Y: {self.y}, kryptis: {self.kryptis}, šūviai: {self.suviai}")

    def siaure(self):
        self.y += 1
        self.kryptis = "Š"
        self._info()

    def pietus(self):
        self.y -= 1
        self.kryptis = "P"
        self._info()

    def vakarai(self):
        self.x -= 1
        self.kryptis = "V"
        self._info()

    def rytai(self):
        self.x += 1
        self.kryptis = "R"
        self._info()

    def sauti(self):
        if self.kryptis == "Š":
            self.suviai[0] += 1
        if self.kryptis == "P":
            self.suviai[1] += 1
        if self.kryptis == "V":
            self.suviai[2] += 1
        if self.kryptis == "R":
            self.suviai[3] += 1
        self._info()
