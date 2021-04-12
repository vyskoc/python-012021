# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas as pd
import matplotlib.pyplot as plt

teplota = pd.read_csv("temperature.csv", index_col=False)
helsinky = teplota[teplota["City"] == "Helsinki"].loc[:,["Day","AvgTemperature"]]
miami = teplota[teplota["City"] == "Miami Beach"].loc[:,["Day","AvgTemperature"]]
tokyo = teplota[teplota["City"] == "Tokyo"].loc[:,["Day","AvgTemperature"]]
helsinky = helsinky.set_index('Day') # SPOJIT JAKO TABULKU????
miami = miami.set_index('Day')
tokyo = tokyo.set_index('Day')
teploty=pd.merge(helsinky, miami, on="Day")
teploty=pd.merge(teploty, tokyo, on="Day")
teploty.rename(columns={"AvgTemperature_x":"Helsinky",
                        "AvgTemperature_y":"Miami",
                        "AvgTemperature":"Tokyo" }, inplace=True)
teploty.plot(kind = "box")
plt.show() #Helsinky nejchaldnější, Miami nejteplejší