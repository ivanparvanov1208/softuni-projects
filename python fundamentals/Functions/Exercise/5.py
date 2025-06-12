def even_nums_list(num = input().split(" ")):
    even_nums_str = filter(lambda x: int(x) % 2 == 0, num)

    even_nums = []

    for digit in even_nums_str:
        even_nums.append(int(digit))

    return list(even_nums)

print(even_nums_list())

