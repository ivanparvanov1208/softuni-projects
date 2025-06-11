numbers_str = input()
n = int(input())

numbers = [int(x) for x in numbers_str.split()]

for _ in range(n):
    if numbers:
        smallest = min(numbers)
        numbers.remove(smallest)

print(", ".join(map(str, numbers)))
