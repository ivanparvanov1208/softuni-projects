product = input()
city = input()
quantity = float(input())
currunt_price = 0

if city == 'Sofia':
    if product == 'coffee':
        currunt_price = 0.50
    elif product == 'water':
        currunt_price = 0.80
    elif product == 'beer':
        currunt_price = 1.20
    elif product == 'sweets':
        currunt_price = 1.45
    elif product == 'peanuts':
        currunt_price = 1.60

elif city == 'Plovdiv':
    if product == 'coffee':
        currunt_price = 0.40
    elif product == 'water':
        currunt_price = 0.70
    elif product == 'beer':
        currunt_price = 1.15
    elif product == 'sweets':
        currunt_price = 1.30
    elif product == 'peanuts':
        currunt_price = 1.50

elif city == 'Varna':
    if product == 'coffee':
        currunt_price = 0.45
    elif product == 'water':
        currunt_price = 0.70
    elif product == 'beer':
        currunt_price = 1.10
    elif product == 'sweets':
        currunt_price = 1.35
    elif product == 'peanuts':
        currunt_price = 1.55

total_price = currunt_price * quantity
print(total_price)