time = int(input())
day = input()

status = ""

if 10 <= time <= 18:
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
        status = "open"
    elif day == "Sunday":
        status = "closed"
else:
    status = "closed"

print(status)