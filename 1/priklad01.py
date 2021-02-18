# Níže máš slovník, který obsahuje kódy balíků s informací, zda již byl balík
# předán kurýrovi k doručení. Pokud byl předán, má hodnotu True, v opačném případě
# má hodnotu False.
# Napiš programpro operátora společnosti, který poskytuje informaci, zda byl balík
# předán kurýrovi. Nejprve se uživatele zeptej na kód balíku. Následně podle hodnoty
# ve slovníku vypiš větu Balík byl předán kurýrovi nebo Balík zatím nebyl předán kurýrovi.

baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kodBaliku = str(input("Zadej kód balíku: "))
if kodBaliku not in baliky:
    print("Kód balíku není v databázi.")
elif baliky[kodBaliku] is True:
    print("Balík byl předán kurýrovi.")
else:
    print("Balík zatím nebyl předán kurýrovi.")