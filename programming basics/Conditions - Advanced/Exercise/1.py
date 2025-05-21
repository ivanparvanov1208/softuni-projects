# Premiere - премиерна прожекция, на цена 12.00 лева;
# Normal - стандартна прожекция, на цена 7.50 лева;
# Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

screeningType = input()
rows = int(input())
columns = int(input())

income = 0

cinemaCapacity = rows * columns

if screeningType == "Premiere":
    income = cinemaCapacity * 12
elif screeningType == "Normal":
    income = cinemaCapacity * 7.50
elif screeningType == "Discount":
    income = cinemaCapacity * 5


print(f"{income:.2f} leva")