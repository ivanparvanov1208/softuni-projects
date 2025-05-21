day = input()

cost = 0

if day == "Monday" or day == "Tuesday" or day == "Friday":
    cost = 12
elif day == "Wednesday" or day == "Thursday":
    cost = 14
elif day == "Saturday" or day == "Sunday":
    cost = 16

print(cost)