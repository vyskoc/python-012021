from datetime import datetime

datum = datetime.strptime(input("Zadej datum: "),"%d.%m.%Y")
kusy = int(input("Zadej počet lístků: "))
zacPrvni = datetime(2021, 7, 1)
zacDruhe = datetime(2021, 8, 11)
konDruhe = datetime(2021, 8, 31)

if datum < zacPrvni or datum > konDruhe:
    print("Mimo sezónu!")
elif datum < zacDruhe:
    cena = kusy * 250
    print(f"Cena za ubytování je {cena} Kč.")
else:
    cena = kusy * 180
    print(f"Cena za ubytování je {cena} Kč.")
