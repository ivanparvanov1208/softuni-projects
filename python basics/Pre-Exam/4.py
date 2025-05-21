from math import ceil

days = int(input())
kmFirstDay = float(input())

kmsForDay = kmFirstDay

allKMs = kmFirstDay

for i in range(days):
    k = int(input())

    kPercent = k / 100

    add = kmsForDay * kPercent

    kmsForDay += add

    allKMs += kmsForDay

if allKMs < 1000:
    diff = 1000 - allKMs
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")
else:
    diff = allKMs - 1000
    print(f"You've done a great job running {ceil(diff)} more kilometers!")