n = int(input())

for _ in range(n):
    string = input()

    is_pure = True

    for letter in string:
        if letter == "_" or letter == "." or letter == ",":
            is_pure = False

    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")