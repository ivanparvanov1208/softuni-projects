budget = float(input())
pricePer1kgFlour = float(input())

priceFor1packEggs = pricePer1kgFlour * 0.75
priceFor1LMilk = pricePer1kgFlour + (pricePer1kgFlour * 0.25)

total = pricePer1kgFlour + priceFor1packEggs + (priceFor1LMilk * 0.25)

breadCount = 0
eggsCount = 0

while True:
    if budget <= total:
        break
    else:
        budget -= total
        breadCount += 1
        eggsCount += 3
        if breadCount % 3 == 0:
            eggsCount -= breadCount - 2

print(f"You made {breadCount} loaves of Easter bread! Now you have {eggsCount} eggs and {budget:.2f}BGN left.")