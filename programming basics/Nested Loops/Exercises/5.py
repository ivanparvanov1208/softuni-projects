n = int(input())
string = ""

for i in range(1111, 10000):
    count = 0
    for index, digit in enumerate(str(i)):
        if int(digit) == 0:
            pass
        elif n % int(digit) == 0:
            count += 1

    if count == 4:
        string += str(i) + " "

print(string)