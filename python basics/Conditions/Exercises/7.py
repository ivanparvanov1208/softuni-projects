'''
Видеокарта – 250 лв./бр.
Процесор – 35% от цената на закупените видеокарти/бр.
Рам памет – 10% от цената на закупените видеокарти/бр.
'''

budget = float(input())
GPUCount = int(input())
CPUCount = int(input())
RAMCount = int(input())

GPUPrice = GPUCount * 250
CPUPrice = CPUCount * (GPUPrice * 0.35)
RAMPrice = RAMCount * (GPUPrice * 0.1)

totalPrice = GPUPrice + CPUPrice + RAMPrice

if GPUPrice > CPUPrice:
    discount = totalPrice * 0.15
    totalPrice -= discount

if totalPrice <= budget:
    print(f"You have {budget - totalPrice:.2f} leva left!")
else:
    print(f"Not enough money! You need {totalPrice - budget:.2f} leva more!")