firstNumber = int(input())
sum = firstNumber

for i in range(3):
    num = int(input())
    if i == 0:
        sum += num
    elif i == 1:
        sum //= num
    elif i == 2:
        sum *= num

print(sum)