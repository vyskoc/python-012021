# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas as pd
import matplotlib.pyplot as plt

teplota = pd.read_csv("temperature.csv")
#vyber = teplota[(teplota["City"] == "Helsinki") | (teplota["City"] == "Miami Beach")| (teplota["City"] == "Tokyo")]
helsinky = teplota[teplota["City"] == "Helsinki"].loc[:,"AvgTemperature"]
miami = teplota[teplota["City"] == "Miami Beach"].loc[:,"AvgTemperature"]
tokyo = teplota[teplota["City"] == "Tokyo"].loc[:,"AvgTemperature"]
print(helsinky, miami, tokyo)
teploty = helsinky.to_frame(name="Helsinky")
teploty["Miami Beach"] = miami
teploty["Tokyo"] = tokyo
print(teploty)
teploty.plot(kind = "box")
plt.show()