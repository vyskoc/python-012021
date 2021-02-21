prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
# co se zdvojenou položkou "zkus mě chytit"?

prodeje = {**prodeje2020, **prodeje2019}
for key, value in prodeje.items():
   if key in prodeje2020 and key in prodeje2019:
           prodeje[key] = value + prodeje2020[key]

kniha = str(input("Zadej název knihy: "))
if kniha not in prodeje:
    print("Knihu jsme vůbec neprodávali.")
else:
    print(prodeje[kniha])
