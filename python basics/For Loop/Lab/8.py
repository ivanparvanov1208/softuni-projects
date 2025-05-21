n = int(input())

if n >= 0:
    first_num = int(input())
    maxNum = first_num
    minNum = first_num

    for i in range(1, n):
        num = int(input())

        if num > maxNum:
            maxNum = num

        if num < minNum:
            minNum = num

    print(f"Max number: {maxNum}")
    print(f"Min number: {minNum}")