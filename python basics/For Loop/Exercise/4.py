age = int(input())
washerCost = float(input())
costPerToy = int(input())

money = 0
toyCount = 0

sum = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        sum += 10
        money += sum
        money -= 1
    elif i % 2 == 1:
        toyCount += 1

toyEarnings = toyCount * costPerToy

money += toyEarnings


if money >= washerCost:
    diff = money - washerCost
    print(f"Yes! {diff:.2f}")
else:
    diff = washerCost - money
    print(f'No! {diff:.2f}')