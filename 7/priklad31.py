# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import pandas as pd
import matplotlib.pyplot as plt
liberec = pd.read_csv("zam_liberec.csv")
plzen = pd.read_csv("zam_plzeň.csv")
praha = pd.read_csv("zam_praha.csv")
platy = pd.read_csv("platy_2021_02.csv", index_col="cislo_zamestnance")
liberec["mesto"] = "Liberec"
plzen["mesto"] = "Plzeň"
praha["mesto"] = "Praha"
zamestnanci = pd.concat([liberec, plzen, praha], ignore_index=True)
zamestnanciSplaty = pd.merge(zamestnanci, platy, on="cislo_zamestnance", how="outer")
print(zamestnanciSplaty)
zamestnanciSplaty.hist(column = "plat", bins=[30_000,35_000, 40_000, 45_000,50_000, 55_000, 60_000], by="mesto")
plt.show()