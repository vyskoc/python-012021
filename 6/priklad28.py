import pandas as pd
gdp = pd.read_csv("gdp.csv")
staty = pd.read_json("staty.json")
#print(staty.columns)
evropa = staty[staty["region"].isin(["Europe"])]
print(evropa.groupby("subregion")["subregion"].size())
print(evropa.groupby("subregion")["population"].sum())
#print(evropa)