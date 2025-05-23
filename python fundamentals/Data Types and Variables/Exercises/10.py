lostFights = int(input())

helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

expenses = 0

shieldBreak = 0

for i in range(1, lostFights + 1):
    if i % 2 == 0:
        expenses += helmetPrice
    if i % 3 == 0:
        expenses += swordPrice
        if i % 2 == 0:
            expenses += shieldPrice
            shieldBreak += 1
    if shieldBreak == 2:
        expenses += armorPrice
        shieldBreak = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")