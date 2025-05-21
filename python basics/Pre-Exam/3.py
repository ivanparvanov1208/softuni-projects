people = int(input())
season = input()

if season == "spring":
    if people <= 5:
        cost = 50
    elif people > 5:
        cost = 48

    total = people * cost
elif season == "summer":
    if people <= 5:
        cost = 48.5
    elif people > 5:
        cost = 45
    total = people * cost
    discount = total * 0.15
    total -= discount
elif season == "autumn":
    if people <= 5:
        cost = 60
    elif people > 5:
        cost = 49.5
    total = people * cost
elif season == "winter":
    if people <= 5:
        cost = 86
    elif people > 5:
        cost = 85

    total = people * cost
    add = total * 0.08
    total += add

print(f"{total:.2f} leva.")