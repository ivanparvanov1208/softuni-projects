groupSize= int(input())
days = int(input())

coins_earned = 0

for current_day in range(1, days + 1):

    if current_day % 10 == 0:
        groupSize -= 2

    if current_day % 15 == 0:
        groupSize += 5

    food_for_the_companions = 2 * groupSize
    daily_earnings = 50 - food_for_the_companions
    coins_earned += daily_earnings

    if current_day % 3 == 0:
        coins_earned -= 3 * groupSize

    if current_day % 5 == 0:
        coins_earned += 20 * groupSize

        if current_day % 3 == 0:
            coins_earned -= 2 * groupSize

coins_per_companion = int(coins_earned / groupSize)

print(f"{groupSize} companions received {coins_per_companion} coins each.")

