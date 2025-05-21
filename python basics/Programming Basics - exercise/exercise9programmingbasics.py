length = int(input())
width = int(input())
height = int(input())
occupiedPercent = float(input())

volumeAquarium = length * width * height

volumeInLiters = volumeAquarium * 0.001

requiredLiters = volumeInLiters * (1 - (occupiedPercent / 100))

print(requiredLiters)