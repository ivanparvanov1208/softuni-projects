groups = int(input())

musalaCount = 0
monblanCount = 0
kilimanjaroCount = 0
k2Count = 0
everestCount = 0

peopleCount = 0


for i in range(groups):
    groupCount = int(input())

    peopleCount += groupCount

    if 1 <= groupCount <= 5:
        musalaCount += groupCount
    elif 6 <= groupCount <= 12:
        monblanCount += groupCount
    elif 13 <= groupCount <= 25:
        kilimanjaroCount += groupCount
    elif 26 <= groupCount <= 40:
        k2Count += groupCount
    elif groupCount >= 41:
        everestCount += groupCount


p1 = musalaCount / peopleCount * 100
p2 = monblanCount / peopleCount * 100
p3 = kilimanjaroCount / peopleCount * 100
p4 = k2Count / peopleCount * 100
p5 = everestCount / peopleCount * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")