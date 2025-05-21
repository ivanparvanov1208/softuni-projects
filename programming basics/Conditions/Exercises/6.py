recordToBreak = float(input())
distance = float(input())
timePerMeter = float(input())

plainTime = distance * timePerMeter

correctedTime = (distance // 15) * 12.5

totalTime = plainTime + correctedTime

if totalTime >= recordToBreak:
    print(f"No, he failed! He was {totalTime - recordToBreak:.2f} seconds slower.")
elif totalTime < recordToBreak:
    print(f"Yes, he succeeded! The new world record is {totalTime:.2f} seconds.")