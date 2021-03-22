"""import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")"""

import pandas as pd
DataFrame = pd.read_csv("character-deaths.csv")
DataFrame = DataFrame.set_index("Name")
print(DataFrame.columns)
print(DataFrame.loc["Hali"])
print(DataFrame.loc["Gevin Harlaw":"Gillam"])
print(DataFrame.loc["Gevin Harlaw":"Gillam"][["Death Year"]])
print(DataFrame.loc["Gevin Harlaw":"Gillam","GoT":"DwD"])