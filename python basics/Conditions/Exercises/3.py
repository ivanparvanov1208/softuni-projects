hours = int(input())
minutes = int(input())

if hours <= 23 and minutes <= 59:
    minutes += 15

    if minutes == 60:
        hours += 1
        minutes = 0
    elif minutes > 60:
        hours += 1
        minutes = minutes - 60

    if hours == 24:
        hours = 0
    elif hours > 24:
        hours = hours // 24

    if minutes < 10:
        print(f"{hours}:0{minutes}")
    else:
        print(f"{hours}:{minutes}")

