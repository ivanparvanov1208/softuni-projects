def is_even(number):
    if number % 2 == 0:
        return True
    return False

list_ = input().split()

for item in list_:
    if is_even(len(item)):
        print(item)