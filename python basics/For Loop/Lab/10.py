n = int(input())

sumOdd = 0
sumEven = 0

for i in range(1, n + 1):
    num = int(input())

    if i % 2 == 0:
        sumEven += num
    elif i % 2 == 1:
        sumOdd += num

if sumEven == sumOdd:
    print(f"Yes\nSum = {sumEven}")
elif sumEven < sumOdd:
    diff = sumOdd - sumEven
    print(f"No\nDiff = {abs(diff)}")
elif sumEven > sumOdd:
    diff = sumEven - sumOdd
    print(f"No\nDiff = {abs(diff)}")