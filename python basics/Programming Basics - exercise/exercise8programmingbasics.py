practiceAnnualFee = int(input())

shoesCost = practiceAnnualFee - (practiceAnnualFee * 0.4)
basketballEquipmentCost = shoesCost - (shoesCost * 0.2)
ballCost = 0.25 * basketballEquipmentCost
accessoriesCost = 0.2 * ballCost

finalCost = practiceAnnualFee + shoesCost + basketballEquipmentCost + ballCost + accessoriesCost

print(finalCost)