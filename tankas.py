class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Š"
        self.suviai = []

    def siaure(self):
        self.y += 1
        self.kryptis = "Š"

    def pietus(self):
        self.y -= 1
        self.kryptis = "P"

    def vakarai(self):
        self.x -= 1
        self.kryptis = "V"

    def rytai(self):
        self.x += 1
        self.kryptis = "R"

