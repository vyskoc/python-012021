#Evidence aut
class Auta:
    def __init__(self,rz, znacka, km):
        self.rz = rz
        self.znacka = znacka
        self.km = km
        self.obsazenost = True #True pokud je volné a False pokud je vypůjčené

a1 = Auta ("4A2 3020", "Peugeot 403 Cabrio", 47534)
a2 = Auta ("1P3 4747", "Škoda Octavia",41253)
print(a1.km)