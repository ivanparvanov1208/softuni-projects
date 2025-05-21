width = int(input())
length = int(input())
height = int(input())

roomArea = width * length * height

while True:
    command = input()

    if command.isdigit():
        carriedBoxes = int(command)
        roomArea -= carriedBoxes

        if roomArea <= 0:
            print(f"No more free space! You need {abs(roomArea)} Cubic meters more.")
            break

    elif command == "Done":
        print(f"{roomArea} Cubic meters left.")
        break