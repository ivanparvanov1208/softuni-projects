def new_version(firstNumber, secondNumber, thirdNumber):
    thirdNumber += 1
    if thirdNumber > 9:
        secondNumber += 1
        thirdNumber = 0
    if secondNumber > 9:
        firstNumber += 1
        secondNumber = 0

    return ".".join([str(firstNumber), str(secondNumber), str(thirdNumber)])


n1, n2, n3 = map(int, input().split("."))
print(new_version(n1, n2, n3))