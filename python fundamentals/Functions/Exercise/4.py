def sum_of_digits(num = int(input())):
    sum_of_odd = 0
    sum_of_even = 0

    for digit in str(num):
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        elif int(digit) == 0:
            continue
        elif int(digit) % 2 != 0:
            sum_of_odd += int(digit)

    return print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")

sum_of_digits()
