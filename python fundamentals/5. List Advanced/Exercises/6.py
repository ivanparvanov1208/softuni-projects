numberOfElectrons = int(input())

filledShells = []

while True:
    last_position = len(filledShells) + 1
    electronsToFill = 2 * (last_position ** 2)

    if numberOfElectrons >= electronsToFill:
        filledShells.append(electronsToFill)
        numberOfElectrons -= electronsToFill
    elif numberOfElectrons == 0:
        break
    else:
        filledShells.append(numberOfElectrons)
        break

print(filledShells)
