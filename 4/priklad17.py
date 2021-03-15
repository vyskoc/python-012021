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
    def get_celkova_delka(self):
        celkovaDelka = self.delka
        return celkovaDelka

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocetE, delkaE):
        super().__init__(nazev, zanr)
        self.pocetE = pocetE
        self.delkaE = delkaE
    def get_info(self):
        return super().get_info() + f"délka: {self.delkaE} min  počet epizod: {self.pocetE}"
    def get_celkova_delka(self):
        celkovaDelka = self.pocetE * self.delkaE
        return celkovaDelka
class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
    def pripocti_zhlednuti(self, delka_sledovani):
        self.delka_sledovani += delka_sledovani
        return self.delka_sledovani
matrix = Polozka ("Matrix", "sci-fi")
alien = Film ("Vetřelec", "sci-fi", 89)
bigBang = Serial ("Big Bang Theory", "komedy", 24, 20)
lucka = Uzivatel("vyskoc")
delka_sledovaniAaB = alien.get_celkova_delka()+bigBang.get_celkova_delka()

print(alien.get_celkova_delka())
print(bigBang.get_celkova_delka())
print(lucka.pripocti_zhlednuti(delka_sledovaniAaB))
print(lucka.pripocti_zhlednuti(delka_sledovaniAaB))
