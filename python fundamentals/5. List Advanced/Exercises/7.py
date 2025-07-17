numbers = [int(number) for number in input().split(", ")]
group = 10
while numbers:
    numbersList = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {numbersList}")
    numbers = [number for number in numbers if number not in numbersList]
    group += 10