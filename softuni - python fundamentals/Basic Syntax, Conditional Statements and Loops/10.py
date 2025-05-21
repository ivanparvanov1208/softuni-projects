string1 = input()
string2 = input()

lastPrinted = string1

for index in range(len(string1)):
    leftPart = string2[:index + 1]
    rightPart = string1[index + 1:]

    new_string = leftPart + rightPart

    if new_string != lastPrinted:
        print(new_string)
        lastPrinted = new_string