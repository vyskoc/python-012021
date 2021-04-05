# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")
twilio["Date"] = pandas.to_datetime(twilio["Date"]) #Date je teď datum a v grafu se dělí po měsících
ax = twilio.plot(x="Date",y="Close", c="red")
ax.set_ylabel("Cena v dolarech")
ax.set_title("Vývoj ceny akcie firmy Twilio")
ax.set_xlabel("Měsíc")
plt.show()