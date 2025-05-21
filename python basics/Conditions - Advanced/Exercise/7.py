month = input()
nights = int(input())

pricePerNightStudio = 0
pricePerNightApartment = 0

if month == "May" or month == "October":
    pricePerNightStudio = 50
    pricePerNightApartment = 65
elif month == "June" or month == "September":
    pricePerNightStudio = 75.20
    pricePerNightApartment = 68.70
elif month == "July" or month == "August":
    pricePerNightStudio = 76
    pricePerNightApartment = 77

if month == "May" or month == "October":
    if nights > 14:
        pricePerNightStudio *= 0.7
    elif nights > 7:
        pricePerNightStudio *= 0.95
elif month == "June" or month == "September":
    if nights > 14:
        pricePerNightStudio *= 0.8

if nights > 14:
    pricePerNightApartment *= 0.9

totalStudio = pricePerNightStudio * nights
totalApartment = pricePerNightApartment * nights

print(f"Apartment: {totalApartment:.2f} lv.")
print(f"Studio: {totalStudio:.2f} lv.")