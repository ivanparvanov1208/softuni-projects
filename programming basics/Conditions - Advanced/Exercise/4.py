# В зависимост от сезона:
# Цената за наем на кораба през пролетта е  3000 лв.;
# Цената за наем на кораба през лятото и есента е  4200 лв.;
# Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# Ако групата е до 6 човека включително  -  отстъпка от 10%;
# Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# Ако групата е от 12 нагоре  -  отстъпка от 25%.

budget = int(input())
season = input()
fishermans = int(input())

price = 0
discount = 0
discount2 = 0

if season == "Spring":
    price = 3000
    if fishermans <= 6:
        discount = price * 0.1
        price -= discount
    elif 7 < fishermans <= 11:
        discount = price * 0.15
        price -= discount
    elif fishermans >= 12:
        discount = price * 0.25
        price -= discount
elif season == "Summer" or season == "Autumn":
    price = 4200
    if fishermans <= 6:
        discount = price * 0.1
        price -= discount
    elif 7 < fishermans <= 11:
        discount = price * 0.15
        price -= discount
    elif fishermans >= 12:
        discount = price * 0.25
        price -= discount
elif season == "Winter":
    price = 2600
    if fishermans <= 6:
        discount = price * 0.1
        price -= discount
    elif 7 < fishermans <= 11:
        discount = price * 0.15
        price -= discount
    elif fishermans >= 12:
        discount = price * 0.25
        price -= discount

if fishermans % 2 == 0 and season != "Autumn":
    discount2 = price * 0.05
    price -= discount2

if budget >= price:
    moneyLeft = budget - price
    print(f"Yes! You have {moneyLeft:.2f} leva left.")
else:
    moneyLeft = price - budget
    print(f"Not enough money! You need {moneyLeft:.2f} leva.")
