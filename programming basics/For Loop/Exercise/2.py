import sys

n = int(input())

max_num = -sys.maxsize
sum_numbers = 0

for i in range(n):
    num = int(input())

    if num > max_num :
        max_num = num

    sum_numbers += num

if max_num == sum_numbers - max_num:
    print(f"Yes\nSum = {max_num}")
else:
    sum_numbers = sum_numbers - max_num
    print(f"No\nDiff = {abs(max_num - sum_numbers)}")