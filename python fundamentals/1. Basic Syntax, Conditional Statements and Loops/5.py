n = int(input())

total = 0

for i in range(n):
    pricePerCap = float(input())
    days = int(input())
    capsulesPer = int(input())

    if pricePerCap < 0.01 or pricePerCap > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsulesPer < 1 or capsulesPer > 2000:
        continue
    else:
        pricePerDay = pricePerCap * capsulesPer

        totalForOrder = pricePerDay * days

        total += totalForOrder

        print(f"The price for the coffee is: ${totalForOrder:.2f}")

print(f"Total: ${total:.2f}")