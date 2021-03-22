"""import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")"""

import pandas as pd
vakciny = pd.read_csv("country_vaccinations.csv")
print(vakciny.columns)

vyber = vakciny[vakciny["date"] == "2021-03-10"]
print(vyber.loc[:][["country","total_vaccinations"]])

vyber2 = vakciny[(vakciny["date"] == "2021-03-10") & (vakciny["daily_vaccinations"]>1_000_000)]
print(vyber2)

vyber3 = vakciny[(vakciny["date"] == "2021-03-10") & ((vakciny["daily_vaccinations"]>100_000) | (vakciny["daily_vaccinations"]<100))]
print(vyber3)