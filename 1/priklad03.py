volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

hodina = int(input("Na jakou hodinu Vám máme rezervovat zasedací místnost: "))
print(f"Máme volné {len(volnePokoje[hodina])} zasedací místnosti.")