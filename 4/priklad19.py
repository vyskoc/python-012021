from forex_python.converter import CurrencyRates
import math
prevodnik = CurrencyRates()
"""pozadovano_v_cilove_mene = 10
cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)"""

zdrojovaMena = input("Zadej zdrojovou měnu: ")
cilovaMena = input("Zadej cílovou měnu: ")
castka = int(input("Zadej požadovanou částku v cílové měně: "))
podil = prevodnik.get_rate(zdrojovaMena, cilovaMena)
pozadovanyZdroj = math.ceil(castka / podil)
print(pozadovanyZdroj)

