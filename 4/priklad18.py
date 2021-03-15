class Kontakt:
    def __init__(self, jmeno, email):
        self.jmeno = jmeno
        self.email = email
class Uchazec(Kontakt):
    def __init__(self, jmeno, email, zapis_z_pohovoru, datum):
        super().__init__(jmeno, email)
        self.zapis_z_pohovoru = zapis_z_pohovoru
        self.datum = datum
    def uloz_zapis(self):
        if datum < datetime.now():
            return self.zapis_z_pohovoru
        else:
            zapis_z_pohovoru = ""
            return "Zápis nebyl zapsán."

zapis_z_pohovoru = input("Zápis: ")
from datetime import datetime
datum = datetime.strptime(input("datum:"), "%d.%m.%Y")
lucka = Uchazec("LucieV", "vyskoc@email.cz",zapis_z_pohovoru,datum)

print(lucka.uloz_zapis())
