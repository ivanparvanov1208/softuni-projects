change = float(input())

coins = 0

change_in_cents = int(round(change * 100))

while change_in_cents > 0:
    if change_in_cents >= 200:
        change_in_cents -= 200
        coins += 1
    elif change_in_cents >= 100:
        change_in_cents -= 100
        coins += 1
    elif change_in_cents >= 50:
        change_in_cents -= 50
        coins += 1
    elif change_in_cents >= 20:
        change_in_cents -= 20
        coins += 1
    elif change_in_cents >= 10:
        change_in_cents -= 10
        coins += 1
    elif change_in_cents >= 5:
        change_in_cents -= 5
        coins += 1
    elif change_in_cents >= 2:
        change_in_cents -= 2
        coins += 1
    elif change_in_cents >= 1:
        change_in_cents -= 1
        coins += 1

print(coins)
