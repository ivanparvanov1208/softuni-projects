def is_special(symbol):
    special_symbols = set("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")

    return symbol in special_symbols

def is_digit(symbol):
    numbers = set("0123456789")
    return symbol in numbers

def check_password(value):
    not_valid = False
    digits_count = 0
    if not 6 <= len(value) <= 10:
        print("Password must be between 6 and 10 characters")
        not_valid = True
    for char in value:
        if is_special(char):
            print("Password must consist only of letters and digits")
            not_valid = True
            break
        elif is_digit(char):
            digits_count += 1

    if digits_count < 2:
        print("Password must have at least 2 digits")
        not_valid = True

    if not not_valid:
        print("Password is valid")

password = input()

check_password(password)
