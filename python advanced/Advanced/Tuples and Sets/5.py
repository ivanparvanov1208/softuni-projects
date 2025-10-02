n = int(input())

longest_intersection_numbers = set()

for _ in range(n):
    first, second = input().split("-")
    first_start, first_end = map(int, first.split(","))
    second_start, second_end = map(int, second.split(","))

    matches = set()

    for i in range(first_start, first_end + 1):
        for j in range(second_start, second_end + 1):
            if i == j:
                matches.add(j)

    if len(matches) > len(longest_intersection_numbers):
        longest_intersection_numbers = matches

print(f"Longest intersection is [{', '.join(map(str, longest_intersection_numbers))}] with length {len(longest_intersection_numbers)}")