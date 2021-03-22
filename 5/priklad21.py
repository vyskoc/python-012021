"""import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")"""

"""Zjisti, kolik má soubor řádek a kolik sloupců.
Podívej se na 5 řádků s cenami na začátku souboru,
 využij k tomu funkci iloc i funkci head().
U akcií nás zajímají především nejnovější ceny.
Podívej se na poslední řádek souboru. Tentokrát využij
způsob dle vlastního výběru :-)"""

import pandas as pd
twlo = pd.read_csv("twlo.csv")
print(twlo.shape)
print(twlo.iloc[:5])
print(twlo.head())
print(twlo.iloc[-1])
