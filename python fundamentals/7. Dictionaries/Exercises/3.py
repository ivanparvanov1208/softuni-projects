countries = input().split(", ")
capitals = input().split(", ")

countriesAndCapitals = {}

for i in range(len(countries)):
    countriesAndCapitals[countries[i]] = capitals[i]

for country, capital in countriesAndCapitals.items():
    print(f"{country} -> {capital}")