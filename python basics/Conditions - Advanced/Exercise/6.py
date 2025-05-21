n1 = int(input())
n2 = int(input())
operation = input()

if operation == "+":
    result = n1 + n2
    evenOrOdd = ""
    if result % 2 == 0:
        evenOrOdd = "even"
    else:
        evenOrOdd = "odd"

    print(f"{n1} {operation} {n2} = {result} - {evenOrOdd}")

elif operation == "-":
    result = n1 - n2
    evenOrOdd = ""
    if result % 2 == 0:
        evenOrOdd = "even"
    else:
        evenOrOdd = "odd"

    print(f"{n1} {operation} {n2} = {result} - {evenOrOdd}")

elif operation == "*":
    result = n1 * n2
    evenOrOdd = ""
    if result % 2 == 0:
        evenOrOdd = "even"
    else:
        evenOrOdd = "odd"

    print(f"{n1} {operation} {n2} = {result} - {evenOrOdd}")


elif operation == "/":
    if n2 != 0:
        result = n1 / n2
        print(f"{n1} {operation} {n2} = {result:.2f}")
    else:
        print(F"Cannot divide {n1} by zero")

elif operation == "%":
    if n2 != 0:
        result = n1 % n2
        print(f"{n1} {operation} {n2} = {result}")
    else:
        print(F"Cannot divide {n1} by zero")
