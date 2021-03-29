import pandas as pd
import pytemperature

teplota = pd.read_csv("temperature.csv")
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
listopad13 = teplota[(teplota["Day"]==13) & (teplota["AvgTemperatureCelsia"] > -70)]
print(teplota.columns)
print(listopad13.groupby("Region")["Region"].size())
print(listopad13.groupby("Region")["AvgTemperatureCelsia"].mean())
print(listopad13.groupby("Region")["AvgTemperatureCelsia"].max())
print(listopad13.groupby("Region")["AvgTemperatureCelsia"].min())
