sum = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        print(f"Total: {sum:.2f}")
        break
    else:
        current_sum = float(command)
        if current_sum < 0:
            print("Invalid operation!")
            print(f"Total: {sum:.2f}")
            break
        else:
            sum += current_sum
            print(f"Increase: {current_sum:.2f}")
