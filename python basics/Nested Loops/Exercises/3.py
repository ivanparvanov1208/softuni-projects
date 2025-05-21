primeSum = 0
nonPrimeSum = 0

while True:
    is_number = False
    is_prime = True
    is_negative = False
    command = input()
    for index, digit in enumerate(command):
        if index == 0 and digit == "-":
            is_number = True
            break
        elif command.isdigit():
            is_number = True

    if is_number:
        number = int(command)

        if number < 0:
            is_negative = True
            print("Number is negative.")
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False

        if is_prime and not is_negative:
            primeSum += number
        elif not is_prime:
            nonPrimeSum += number
    elif command == "stop":
        break

print(f"Sum of all prime numbers is: {primeSum}\nSum of all non prime numbers is: {nonPrimeSum}")