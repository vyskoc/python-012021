"""Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a
příkladu 12.

Přidej třídě Auto funkci vrat_auto(), která bude mít
(krom obligátního self) 2 parametry, a to je stav tachometru
 při vrácení a počet dní, po které zákazník auto používal.
 Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den,
 pokud měl zákazník celkem auto méně než týden, a 300 Kč na den,
pokud měl zákazník auto déle. Cena je stejná pro obě auta.
Vlož cenu do nějakého informativního textu a ten vrať pomocí
klíčového slova return.

Na konec programu (mimo třídu) přidej dotaz na uživatele,
kolik kilometrů zákazník ujel a jak dlouo ho měl půjčené.
Poté vypiš informaci o ceně."""

class Auta:
    def __init__(self,rz, znacka, km):
        self.rz = rz
        self.znacka = znacka
        self.km = km
        self.obsazenost = True #True pokud je volné a False pokud je vypůjčené

    def pujc_auto(self):
        if self.obsazenost:
            self.obsazenost = False
            return f"{self.get_info()} Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        return f"RZ vozidla je {self.rz} a jedná se o {self.znacka}."

    def vrat_auto(self, tachometr, dny):
        self.tachometr = tachometr
        self.obsazenost = True
        self.dny = dny
        if dny > 7:
            cena = dny * 300
        else:
            cena = dny * 400
        return f"Cena za půjčení {self.znacka} za {dny} dní je {cena} Kč."
a1 = Auta ("4A2 3020", "Peugeot 403 Cabrio", 47534)
a2 = Auta ("1P3 4747", "Škoda Octavia",41253)

def dotaz(zadost):
    if zadost in a1.znacka:
        return a1.pujc_auto()
    elif zadost in a2.znacka:
        return a2.pujc_auto()
    else:
        return "Auto není v systému."

zadost = input("Jaké vozidlo si přejete půjčit: ")
print(dotaz(zadost))

tachometr = int(input("Zadej stav tachometru: "))
dny = int(input("Zadej počet dní: "))
print(a1.vrat_auto(tachometr, dny))
