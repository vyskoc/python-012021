# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import pandas as pd
import matplotlib.pyplot as plt

velikonoce = pd.read_csv("velikonoce.csv")
ax = velikonoce.plot(kind = "bar", x = "Datum")
ax.set_ylabel("Počet velikonoc")
ax.set_title("Velikonoce v letech 1600 až 2100")
ax.set_xlabel("Den")
plt.show()