steps = 0
goal = 10000

while steps < goal:
    command = input()

    if command.isdigit():
        walkedSteps = int(command)
        steps += walkedSteps

    elif command == "Going home":
        stepsToHome = int(input())
        steps += stepsToHome
        if steps < goal:
            print(f"{goal - steps} more steps to reach goal.")
        else:
            print(f"Goal reached! Good job!\n{steps - goal} steps over the goal!")
        break

else:
    print(f"Goal reached! Good job!\n{steps - goal} steps over the goal!")