n = int(input())

sum = 0

for _ in range(n):
    symbol = input()
    asciiCode = ord(symbol)

    sum += asciiCode

print(f"The sum equals: {sum}")