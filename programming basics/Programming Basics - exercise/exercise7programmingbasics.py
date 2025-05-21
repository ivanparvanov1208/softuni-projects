chickenMenu = int(input())

fishMenu = int(input())

veganMenu = int(input())

chickenMenuCost = chickenMenu * 10.35
fishMenuCost = fishMenu * 12.40
veganMenuCost = veganMenu * 8.15
costWithoutDeliveryFee = chickenMenuCost + fishMenuCost + veganMenuCost + ((chickenMenuCost + fishMenuCost + veganMenuCost) * 0.2)
finalCost = costWithoutDeliveryFee + 2.50

print(finalCost)