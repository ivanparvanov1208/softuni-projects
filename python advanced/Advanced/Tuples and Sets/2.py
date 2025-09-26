line = input().strip()
n, m = map(int, line.split())

first_set = set()
for _ in range(n):
    num = int(input().strip())
    first_set.add(num)

second_set = set()
for _ in range(m):
    num = int(input().strip())
    second_set.add(num)

common = first_set & second_set

for num in common:
    print(num)
