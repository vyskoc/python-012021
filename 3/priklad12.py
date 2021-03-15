#Půjčení auta

class Auta:
    def __init__(self,rz, znacka, km):
        self.rz = rz
        self.znacka = znacka
        self.km = km
        self.obsazenost = True #True pokud je volné a False pokud je vypůjčené

    def pujc_auto(self):
        if self.obsazenost:
            print("Potvrzuji zapůjčení vozidla")
            print(self.get_info())
            self.obsazenost = False
        else:
            print("Vozidlo není k dispozici")

    def get_info(self):
        print(f"RZ vozidla je {self.rz} a jedná se o {self.znacka}.")

    def dotaz(self):
        zadost = input("Jaké vozidlo si přejete půjčit: ")
        if zadost in self.znacka:
            print(self.pujc_auto())
a1 = Auta ("4A2 3020", "Peugeot 403 Cabrio", 47534)
a2 = Auta ("1P3 4747", "Škoda Octavia",41253)

print(a1.dotaz())
print(a1.dotaz())
#print(a1.pujc_auto())


#zadost = input("Jaké vozidlo si přejete půjčit: ")
#
# if zadost in a2.znacka:
#     print("ok")


