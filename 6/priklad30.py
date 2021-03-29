import pandas as pd

liberec = pd.read_csv("zam_liberec.csv")
plzen = pd.read_csv("zam_plzeň.csv")
praha = pd.read_csv("zam_praha.csv")
platy = pd.read_csv("platy_2021_02.csv")
vykazy = pd.read_csv("vykazy.csv")
liberec["mesto"] = "Liberec"
plzen["mesto"] = "Plzeň"
praha["mesto"] = "Praha"
zamestnanci = pd.concat([liberec, plzen, praha], ignore_index=True)
zamestnanciSplaty = pd.merge(zamestnanci, platy, on="cislo_zamestnance", how="outer")
vykazyZamestnancu = pd.merge(zamestnanciSplaty, vykazy, left_on="cislo_zamestnance", right_on="emloyee_id")
poctyHodin = vykazyZamestnancu.groupby(["project", "mesto"])["hours"].sum()
poctyHodin.to_excel("poctyHodin.xlsx", index=True)
poctyHodinNactene = pd.read_excel("poctyHodin.xlsx", header=1)
print(poctyHodinNactene)