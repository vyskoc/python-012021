# Maturita
vysledky = [
    {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
    {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
    {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
    {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
    {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

poradi = 0
for radky in vysledky:
    radek = (vysledky[poradi])
    prumer = 0
    maximum = 0
    jmeno = radek["Jméno"]
    radek.pop("Jméno")
    for klic, hodnota in radek.items():
        prumer += hodnota / 5
        if hodnota > maximum:
            maximum = hodnota
    if prumer < 1.5 and maximum < 3:
        hodnoceni = "Prospěl s vyznamenáním"
    elif maximum < 5:
        hodnoceni = "Prospěl"
    else:
        hodnoceni = "Neprospěl"
    print(f"{jmeno}: {hodnoceni}")
    poradi +=1

