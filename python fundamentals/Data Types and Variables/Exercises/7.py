n = int(input())

litersPoured = 0

for i in range(n):
    liters = int(input())

    if litersPoured + liters > 255 or litersPoured > 255:
        print("Insufficient capacity!")
    else:
        litersPoured += liters


print(litersPoured)