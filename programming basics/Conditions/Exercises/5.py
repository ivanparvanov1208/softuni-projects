budget = float(input())
countExtras = int(input())
outfitsExtrasPrice = float(input())

decorationPrice = budget * 0.1

allOutfitsPrice = countExtras * outfitsExtrasPrice
if countExtras > 150:
    discountExtras = allOutfitsPrice * 0.1
    allOutfitsPrice -= discountExtras

totalPrice = allOutfitsPrice + decorationPrice

if totalPrice > budget:
    print(f"Not enough money!\nWingard needs {totalPrice - budget:.2f} leva more.")
elif totalPrice <= budget:
    print(f"Action!\n Wingard starts filming with {budget - totalPrice:.2f} leva left.")

