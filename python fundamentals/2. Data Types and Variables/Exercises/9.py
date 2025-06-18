n = int(input())

highestValue = 0
highestValueTime = 0
highestValueWeight = 0
highestValueQuality = 0

for i in range(n):
    weight = int(input())
    timeRequired = int(input())
    quality = int(input())

    value = (weight // timeRequired) ** quality

    if highestValue < value:
        highestValue = value
        highestValueTime = timeRequired
        highestValueWeight = weight
        highestValueQuality = quality

print(f"{highestValueWeight} : {highestValueTime} = {highestValue} ({highestValueQuality})")