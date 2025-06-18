numbers_str = input()
beggar_count = int(input())

numbers = [int(x) for x in numbers_str.split(", ")]
earnings = [0] * beggar_count

for i, num in enumerate(numbers):
    beggar_index = i % beggar_count
    earnings[beggar_index] += num

print(earnings)