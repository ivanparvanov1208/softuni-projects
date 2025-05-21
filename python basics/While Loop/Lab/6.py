started = False

while True:
    command = input()
    if command != "Stop":
        num = int(command)
        if not started:
            maxNum = num
            started = True
        else:
            if maxNum < num:
                maxNum = num
    else:
        print(maxNum)
        break
