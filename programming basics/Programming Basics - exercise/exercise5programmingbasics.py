#Пакет химикали - 5.80 лв.
#Пакет маркери - 7.20 лв.
#Препарат - 1.20 лв (за литър)

# (pencilsCost + markersCost + whiteBoardCleaningCost) - discount

pencils = int(input())

markers = int(input())

litersOfWhiteboardCleaning = int(input())

discount = int(input())

pencilsCost = pencils * 5.80

markersCost = markers * 7.20

whiteBoardCleaningCost = litersOfWhiteboardCleaning * 1.20

allCost = markersCost + pencilsCost + whiteBoardCleaningCost

discountAmount = allCost * (discount / 100)

finalCost = allCost - discountAmount

print(finalCost)
