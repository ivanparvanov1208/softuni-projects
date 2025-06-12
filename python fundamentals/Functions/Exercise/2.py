def add_and_subtract(num1 = int(input()), num2 = int(input()), num3 = int(input())):
    def sum_numbers():
        return num1 + num2
    def subtract():
        return sum_numbers() - num3

    print(subtract())

add_and_subtract()

