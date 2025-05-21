firstNum = int(input())
secondNum = int(input())

for number in range(firstNum, secondNum + 1):
    strNumber = str(number)
    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(strNumber):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=" ")