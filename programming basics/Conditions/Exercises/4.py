tourPrice = float(input())
puzzleCount = int(input())
talkingDollsCount = int(input())
toyBearsCount = int(input())
minionsCount = int(input())
trucksCount = int(input())

totalCountToys = puzzleCount + talkingDollsCount + toyBearsCount + minionsCount + trucksCount

puzzlePrice = puzzleCount * 2.6
talkingDollsPrice = talkingDollsCount * 3
toyBearsPrice = toyBearsCount * 4.1
minionsPrice = minionsCount * 8.2
trucksPrice = trucksCount * 2
totalPrice = puzzlePrice + talkingDollsPrice + toyBearsPrice + minionsPrice + trucksPrice

if totalCountToys >= 50:
    discount = totalPrice * 0.25
    totalPrice -= discount

rent = totalPrice * 0.1
totalPrice -= rent

if tourPrice <= totalPrice:
    print(f"Yes! {totalPrice - tourPrice:.2f} lv left.")
else:
    print(f"Not enough money! {tourPrice - totalPrice:.2f} lv needed.")