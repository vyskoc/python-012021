#Klíč k úspěchu

odvetvi = input("Odvětví: ")
obrat = int(input("Obrat (mil. €): "))
zeme = str(input("Země: "))
konference = input("Konference: ")
news = input("Newsletter: ")

uspech = 0

def posOdvetvi(odvetvi):
    uspechO = 0
    if odvetvi == "automotive":
        uspechO = 3
    elif odvetvi == "retail":
        uspechO = 2
    return  uspechO

def posObrat(obrat):
    if obrat <= 10:
        uspechOb = 0
    elif obrat <= 1000:
        uspechOb = 3
    else:
        uspechOb = 1
    return uspechOb

def posZeme(zeme):
    if zeme == "Slovensko" or zeme == "Česko":
        uspechZ = 2
    elif zeme == "Německo" or zeme == "Francie":
        uspechZ = 1
    else:
        uspechZ = 0
    return uspechZ

def posKonference(konference = False):
    uspechK = 0
    if konference:
        uspechK = 1
    return uspechK

def posNews(news = False):
    uspechN = 0
    if news:
        uspechN = 1
    return uspechN

uspech = posOdvetvi(odvetvi) + posObrat(obrat) + posZeme(zeme) + posKonference(konference) + posNews(news)

if uspech <= 5:
    posouzeni = "malá"
elif uspech <= 8:
    posouzeni = "střední"
else:
    posouzeni = "velká"

print(f"Zakázka dosahla {uspech} bodů, šance na záskání je {posouzeni}.")

