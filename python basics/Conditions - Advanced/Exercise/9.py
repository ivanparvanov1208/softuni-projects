# "room for one person" – 18.00 лв за нощувка
# "apartment" – 25.00 лв за нощувка
# "president apartment" – 35.00 лв за нощувка

daysStay = int(input())
premise = input()
grade = input()

discountGrade = 0
discountApartment = 0
discountPresidentApartment = 0
nights = daysStay - 1
priceRoomForOne = nights * 18
priceApartment = nights * 25
pricePresidentApartment = nights * 35

if premise == "room for one person":
    totalPrice = priceRoomForOne

elif premise == "apartment":
    if nights < 10:
        discountApartment = priceApartment * 0.3
    elif nights < 15:
        discountApartment = priceApartment * 0.35
    elif nights >= 15:
        discountApartment = priceApartment * 0.5

    priceApartment -= discountApartment

    totalPrice = priceApartment
elif premise == "president apartment":

    if nights < 10:
        discountPresidentApartment = pricePresidentApartment * 0.1
    elif 10 <= nights < 15:
        discountPresidentApartment = pricePresidentApartment * 0.15
    elif nights >= 15:
        discountPresidentApartment = pricePresidentApartment * 0.2

    pricePresidentApartment -= discountPresidentApartment

    totalPrice = pricePresidentApartment

if grade == "positive":
    discountGrade = totalPrice * 0.25
    totalPrice += discountGrade
elif grade == "negative":
    discountGrade = totalPrice * 0.1
    totalPrice -= discountGrade

print(f"{totalPrice:.2f}")