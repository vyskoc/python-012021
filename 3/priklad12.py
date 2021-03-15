#Půjčení auta

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

a1 = Auta ("4A2 3020", "Peugeot 403 Cabrio", 47534)
a2 = Auta ("1P3 4747", "Škoda Octavia",41253)

def dotaz(zadost):
    if zadost in a1.znacka:
        return a1.pujc_auto()
    elif zadost in a2.znacka:
        return a2.pujc_auto()
    else:
        return "Auto není v systému."

print(dotaz(input("Jaké vozidlo si přejete půjčit: ")))
print(dotaz(input("Jaké vozidlo si přejete půjčit: ")))



