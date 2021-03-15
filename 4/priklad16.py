class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    def get_info(self):
        return f"Název: {self.nazev}  žánr: {self.zanr} "
class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def get_info(self):
        return super().get_info() + f"délka: {self.delka} min"

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocetE, delkaE):
        super().__init__(nazev, zanr)
        self.pocetE = pocetE
        self.delkaE = delkaE
    def get_info(self):
        return super().get_info() + f"délka: {self.delkaE} min  počet epizod: {self.pocetE}"

matrix = Polozka ("Matrix", "sci-fi")
alien = Film ("Vetřelec", "sci-fi", 89)
bigBang = Serial ("Big Bang Theory", "komedy", 24, 20)
print(matrix.get_info())
print(alien.get_info())
print(bigBang.get_info())


