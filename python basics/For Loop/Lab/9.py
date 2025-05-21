n = int(input())

sum1 = 0
sum2 = 0

for i in range(n):
    num = int(input())
    sum1 += num


for j in range(n):
    num2 = int(input())
    sum2 += num2

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    if sum1 < sum2:
        diff = sum2 - sum1
    else:
        diff = sum1 - sum2
    print(f"No, diff = {diff}")