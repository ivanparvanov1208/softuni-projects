
floors = int(input())
rooms = int(input())

string = ""

for floor in range(floors, 0, -1):
    if floor == floors:
        letter = "L"
    elif floor % 2 == 0:
        letter = "O"
    elif floor % 2 == 1:
        letter = "A"
    for room in range(0, rooms):
        string += f"{letter}{floor}{room} "
    string += "\n"

print(string)