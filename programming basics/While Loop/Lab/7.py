started = False

while True:
    command = input()
    if command != "Stop":
        num = int(command)
        if not started:
            minNum = num
            started = True
        else:
            if minNum > num:
                minNum = num
    else:
        print(minNum)
        break