numbersInput = input().split(" ")

newList = []

numbersList = list(numbersInput)

for number in numbersList:
    newList.append(int(number) - (int(number) * 2))

print(newList)
