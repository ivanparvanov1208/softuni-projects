nylonRequiredSquareMeters = int(input())

paintRequiredLiters = int(input())

diluentRequiredLiters = int(input())

hoursDue = int(input())

nylonCost = (2 + nylonRequiredSquareMeters) * 1.50
paintCost = (paintRequiredLiters + (paintRequiredLiters * 0.1)) * 14.50
diluentCost = diluentRequiredLiters * 5.00
allMaterialsCost = nylonCost + paintCost + diluentCost + 0.40
workersWage = (allMaterialsCost * 0.3) * hoursDue
finalCost = allMaterialsCost + workersWage

print(finalCost)
