#SMS brána
"""
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné
(pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí
hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné,
vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou
vypíše uživateli.

Tip: Zkus svoji první funkci vytunit tak, že si bude umět poradit s mezerami v telefonním čísle.
Mezer se zbavíš tak, že použiješ funkci replace() a tečkovou notaci. První parametr je znak,
který chceš nahradit, a druhý parametr nový znak. Níže je příklad použití.

tel_cislo = "+420 734 123 456"
tel_cislo = tel_cislo.replace(" ", "")
"""
tel_cislo = input("Zadej telefonní číslo: ")

def overeniCisla(tel_cislo):
    tel_cislo = tel_cislo.replace(" ", "")
    delkaCisla = len(tel_cislo)
    if delkaCisla == 13 or delkaCisla == 9:
        odpoved = True
    else:
        odpoved = False
    return odpoved

def vypocetCeny(text):
    import math
    delkaTextu = math.ceil(len(text) / 180)
    return delkaTextu * 3

if overeniCisla(tel_cislo):
    text = input("Zadej text zprávy: ")
    print(f"Cena za zprávu je {vypocetCeny(text)} Kč.")
else:
    print(overeniCisla(tel_cislo))

