import pandas as pd
teplota = pd.read_csv("temperature.csv")
print(teplota.head())

listopad = teplota[teplota["Day"]==13]
print(listopad)

listopadUs = teplota[(teplota["Day"]==13) & (teplota["Country"]=="US")]
print(listopadUs)

WaP = listopadUs[(listopadUs["City"] == "Washington") | (listopadUs["City"] == "Philadelphia")]
print(WaP)

print("Průměr teplot: ", listopadUs["AvgTemperature"].mean())
print("Medián teplot: ", listopadUs["AvgTemperature"].median())
print("Rozptyl teplot: ",listopadUs["AvgTemperature"].var())