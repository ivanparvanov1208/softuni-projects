divisor = int(input())
boundary = int(input())

largest = 0

for i in range(boundary + 1):
    if i % divisor == 0:
        largest = i

print(largest)