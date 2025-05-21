starterPoints = int(input())

bonusPoints = 0

if starterPoints <= 100:
    bonusPoints = 5
elif 100 < starterPoints <= 1000:
    bonusPoints = starterPoints * 0.2
else:
    bonusPoints = starterPoints * 0.1

if starterPoints % 2 == 0:
    bonusPoints += 1
elif starterPoints % 10 == 5:
    bonusPoints += 2

totalPoints = starterPoints + bonusPoints

print(f"{bonusPoints}\n{totalPoints}")

