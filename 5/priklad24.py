"""import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")"""

import pandas as pd
teplota = pd.read_csv("temperature.csv")
print(teplota.head())
praha = teplota[teplota["City"] == "Prague"]
print(praha) #teplota je ve F?

teplo = teplota[(teplota["AvgTemperature"]>60) & (teplota["Region"]=="Europe")]
print(teplo)

extremy = teplota[(teplota["AvgTemperature"]>80) | (teplota["AvgTemperature"]<-20)]
print(extremy)

import pytemperature
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
#print(teplota.tail())
teploC = teplota[(teplota["AvgTemperatureCelsia"]>30)]
print(teploC)

teploCE = teplota[(teplota["AvgTemperatureCelsia"]>15) & (teplota["Region"]=="Europe")]
print(teploCE)

extremyC = teplota[(teplota["AvgTemperatureCelsia"]>30) | (teplota["AvgTemperatureCelsia"]<-10)]
print(extremyC) # -99F je asi chyba teploměru nebo nebyl v provozu?
