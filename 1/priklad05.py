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

kniha = str(input("Zadej název knihy: "))
if kniha not in prodeje2020:
    if kniha not in prodeje2019:
        print("Knihu jsme vůbec neprodávali.")
elif kniha not in prodeje2020:
    print(prodeje2019[kniha])
elif kniha not in prodeje2019:
    print(prodeje2020[kniha])
else:
    print(prodeje2019[kniha]+prodeje2020[kniha])