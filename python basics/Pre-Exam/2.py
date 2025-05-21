from math import ceil

daysOfAbsence = int(input())
foodInKG = int(input())
foodPerDayFor1stDeer = float(input())
foodPerDayFor2ndDeer = float(input())
foodPerDayFor3rdDeer = float(input())

firstDeerTotal = daysOfAbsence * foodPerDayFor1stDeer
secondDeerTotal = daysOfAbsence * foodPerDayFor2ndDeer
thirdDeerTotal = daysOfAbsence * foodPerDayFor3rdDeer

totalForAll = firstDeerTotal + secondDeerTotal + thirdDeerTotal

if totalForAll <= foodInKG:
    diff = foodInKG - totalForAll
    diff = ceil(diff)
    print(f"{diff} kilos of food left.")
else:
    diff = totalForAll - foodInKG
    diff = ceil(diff)
    print(f"{diff} more kilos of food are needed.")