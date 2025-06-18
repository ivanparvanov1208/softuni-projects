n = int(input())
p = int(input())

courses = 0

while n > 0:
    n -= p
    courses += 1

print(courses)