n = int(input())
unique = set()
for _ in range(n):
    line = input().strip()
    for el in line.split():
        unique.add(el)
for el in sorted(unique):
    print(el)

