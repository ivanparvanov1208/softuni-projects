fuel = input()
quantity_fuel = float(input())
card = input()

p_gas = 0.93
p_d = 2.33
price_gasol = 2.22

normal_price_diesel = p_d * quantity_fuel
normal_price_gas = p_gas * quantity_fuel
normal_price_gasoline = price_gasol * quantity_fuel

dis_price_gas = p_gas - 0.08
dis_price_diesel = p_d - 0.12
dis_price_gasoline = price_gasol - 0.18

final_price_with_card_diesel = quantity_fuel * dis_price_diesel
final_price_with_card_gas = quantity_fuel * dis_price_gas
final_price_with_card_gasoline = quantity_fuel * dis_price_gasoline

between_20_25 = 8 / 100
over_25_dis = 10 / 100

total = 0

if quantity_fuel < 20 and card == 'Yes' and fuel == "Gas":
    total = final_price_with_card_gas
elif quantity_fuel < 20 and card == 'Yes' and fuel == "Diesel":
    total = final_price_with_card_diesel
elif quantity_fuel < 20 and card == 'Yes' and fuel == "Gasoline":
    total = final_price_with_card_gasoline
if quantity_fuel < 20 and card == 'No' and fuel == "Gas":
    total = normal_price_gas
elif quantity_fuel < 20 and card == 'No' and fuel == "Diesel":
    total = normal_price_diesel
elif quantity_fuel < 20 and card == 'No' and fuel == "Gasoline":
    total = normal_price_gasoline
if 20 <= quantity_fuel <= 25 and card == 'Yes' and fuel == 'Gas':
    total = final_price_with_card_gas * (1 - between_20_25)
elif 20 <= quantity_fuel <= 25 and card == 'Yes' and fuel == 'Diesel':
    total = final_price_with_card_diesel * (1 - between_20_25)
elif 20 <= quantity_fuel <= 25 and card == 'Yes' and fuel == 'Gasoline':
    total = final_price_with_card_gasoline * (1 - between_20_25)
if 20 <= quantity_fuel <= 25 and card == 'No' and fuel == 'Gas':
    total = normal_price_gas * (1 - between_20_25)
elif 20 <= quantity_fuel <= 25 and card == 'No' and fuel == 'Diesel':
    total = normal_price_diesel * (1 - between_20_25)
elif 20 <= quantity_fuel <= 25 and card == 'No' and fuel == 'Gasoline':
    total = normal_price_gasoline * (1 - between_20_25)
if quantity_fuel > 25 and card == 'Yes' and fuel == 'Gas':
    total = final_price_with_card_gas * (1 - over_25_dis)
elif quantity_fuel > 25 and card == 'Yes' and fuel == 'Diesel':
    total = final_price_with_card_diesel * (1 - over_25_dis)
elif quantity_fuel > 25 and card == 'Yes' and fuel == 'Gasoline':
    total = final_price_with_card_gasoline * (1 - over_25_dis)
if quantity_fuel > 25 and card == 'No' and fuel == 'Gas':
    total = normal_price_gas * (1 - over_25_dis)
elif quantity_fuel > 25 and card == 'No' and fuel == 'Diesel':
    total = normal_price_diesel * (1 - over_25_dis)
elif quantity_fuel > 25 and card == 'No' and fuel == 'Gasoline':
    total = normal_price_gasoline * (1 - over_25_dis)


print(f'{total:.2f} lv.')