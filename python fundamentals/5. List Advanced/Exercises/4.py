def categorize_numbers(input_string):
    numbers = list(map(int, input_string.split(", ")))

    positive_numbers = [num for num in numbers if num >= 0]
    negative_numbers = [num for num in numbers if num < 0]
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    print("Positive:", ", ".join(map(str, positive_numbers)))
    print("Negative:", ", ".join(map(str, negative_numbers)))
    print("Even:", ", ".join(map(str, even_numbers)))
    print("Odd:", ", ".join(map(str, odd_numbers)))

input_string = input()
categorize_numbers(input_string)
