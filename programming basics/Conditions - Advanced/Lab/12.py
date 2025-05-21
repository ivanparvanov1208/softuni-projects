city = input()
sales = float(input())

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
        commissionValue = sales * commission
    elif 500 < sales <= 1000:
        commission = 0.07
        commissionValue = sales * commission
    elif 1000 < sales <= 10000:
        commission = 0.08
        commissionValue = sales * commission
    elif sales > 10000:
        commission = 0.12
        commissionValue = sales * commission
    else:
        commissionValue = "error"

elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
        commissionValue = sales * commission
    elif 500 < sales <= 1000:
        commission = 0.075
        commissionValue = sales * commission
    elif 1000 < sales <= 10000:
        commission = 0.1
        commissionValue = sales * commission
    elif sales > 10000:
        commission = 0.13
        commissionValue = sales * commission
    else:
        commissionValue = "error"

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
        commissionValue = sales * commission
    elif 500 < sales <= 1000:
        commission = 0.08
        commissionValue = sales * commission
    elif 1000 < sales <= 10000:
        commission = 0.12
        commissionValue = sales * commission
    elif sales > 10000:
        commission = 0.145
        commissionValue = sales * commission
    else:
        commissionValue = "error"

else:
    commissionValue = "error"

try:
    print(f"{commissionValue:.2f}")
except ValueError:
    print(commissionValue)