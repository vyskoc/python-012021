#Klíč k úspěchu

odvetvi = input("Odvětví: ")
obrat = int(input("Obrat (mil. €): "))
zeme = input("Země: ")
konference = input("Konference: ")
news = input("Newsletter: ")

def parametry(odvetvi, obrat, zeme, konference, news):
    uspech = 0
    if odvetvi == "automotive":
        uspech += 3
    elif odvetvi == "retail":
        uspech += 2
    if obrat <= 10:
        uspech += 0
    elif obrat <= 1000:
        uspech += 3
    else:
        uspech += 1
    if zeme == "Slovensko" or zeme == "Česko":
        uspech += 2
    elif zeme == "Německo" or zeme == "Francie":
        uspech += 1
    if konference:
        uspech += 1
    if news:
        uspech += 1
    if uspech <= 5:
        posouzeni = "malá"
    elif uspech <= 8:
        posouzeni = "střední"
    else:
        posouzeni = "velká"
    return print(f"Zakázka dosahla {uspech} bodů, šance na záskání je {posouzeni}.")

parametry(odvetvi, obrat,zeme, konference, news)

