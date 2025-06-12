def is_perfect(number):
    divisors_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_sum += i

    if divisors_sum / 2 == number:
        return True
    else:
        return False

num = int(input())
if is_perfect(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")