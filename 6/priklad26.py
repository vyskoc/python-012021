import pandas as pd
liberec = pd.read_csv("zam_liberec.csv")
plzen = pd.read_csv("zam_plzeň.csv")
praha = pd.read_csv("zam_praha.csv")
platy = pd.read_csv("platy_2021_02.csv")
liberec["mesto"] = "Liberec"
plzen["mesto"] = "Plzeň"
praha["mesto"] = "Praha"
zamestnanci = pd.concat([liberec, plzen, praha], ignore_index=True)
zamestnanciSplaty = pd.merge(zamestnanci, platy, on="cislo_zamestnance", how="outer")
nepracuji = zamestnanciSplaty[zamestnanciSplaty["plat"].isnull()]
print(nepracuji)
print(zamestnanciSplaty.groupby("mesto")["plat"].mean())