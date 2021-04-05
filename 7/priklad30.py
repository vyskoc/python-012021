# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

# příklad 30 už jsme měli v 6. týdnu
# VELMI PODOBNÉ ZADÁDNÍ JAKO PŘÍKLAD 29

import pandas as pd
import pytemperature

teplota = pd.read_csv("temperature.csv")
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
listopad13 = teplota[(teplota["Day"]==13) & (teplota["AvgTemperatureCelsia"] > -70)]
#print(teplota.columns)
listopad13vz = listopad13.sort_values(["AvgTemperatureCelsia"])
print(listopad13vz.iloc[:5, 3:7])
listopad13se = listopad13.sort_values(["AvgTemperatureCelsia"], ascending =False)
print(listopad13se.iloc[:5,3:7])