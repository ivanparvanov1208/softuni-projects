bestPlayer = ""
maxGoals = 0

while True:
    name = input()
    if name == "END":
        break

    goals = int(input())

    if goals >= 10:
        bestPlayer = name
        maxGoals = goals
        break

    if goals > maxGoals:
        bestPlayer = name
        maxGoals = goals

if bestPlayer:
    print(f"{bestPlayer} is the best player!")
    if maxGoals >= 3:
        print(f"He has scored {maxGoals} goals and made a hat-trick !!!")
    else:
        print(f"He has scored {maxGoals} goals.")