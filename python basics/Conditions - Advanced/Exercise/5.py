budget = float(input())
season = input()

destination = ""
typeVacation = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        typeVacation = "Camp"
    elif season == "winter":
        price = budget * 0.7
        typeVacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        typeVacation = "Camp"
    elif season == "winter":
        price = budget * 0.8
        typeVacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    if season == "summer":
        typeVacation = "Hotel"
    elif season == "winter":
        typeVacation = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}\n{typeVacation} - {price:.2f}")