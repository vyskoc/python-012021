import pandas as pd
vykazy = pd.read_csv("vykazy.csv")
#print(vykazy)
print(vykazy.groupby("project")["hours"].sum())

liberec = pd.read_csv("zam_liberec.csv")
plzen = pd.read_csv("zam_plzeň.csv")
praha = pd.read_csv("zam_praha.csv")
platy = pd.read_csv("platy_2021_02.csv")
liberec["mesto"] = "Liberec"
plzen["mesto"] = "Plzeň"
praha["mesto"] = "Praha"
zamestnanci = pd.concat([liberec, plzen, praha], ignore_index=True)
zamestnanciSplaty = pd.merge(zamestnanci, platy, on="cislo_zamestnance", how="outer")
vykazyZamestnancu = pd.merge(zamestnanciSplaty, vykazy, left_on="cislo_zamestnance", right_on="emloyee_id")
#print(vykazyZamestnancu.columns)
#vykazyZamestnancu.to_csv("vykazyZamestnancu.csv", index=False)
print(vykazyZamestnancu.groupby(["project", "mesto"])["hours"].sum())