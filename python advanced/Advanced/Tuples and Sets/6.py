def solve_names_ascii():
    N = int(input())

    odd_set = set()
    even_set = set()

    for row in range(1, N + 1):
        name = input()

        ascii_sum = sum(ord(char) for char in name)

        result_number = ascii_sum // row

        if result_number % 2 == 0:
            even_set.add(result_number)
        else:
            odd_set.add(result_number)

    sum_odd = sum(odd_set)
    sum_even = sum(even_set)

    final_set = set()

    if sum_odd == sum_even:
        final_set = odd_set.union(even_set)
    elif sum_odd > sum_even:
        final_set = odd_set.difference(even_set)
    else:
        final_set = odd_set.symmetric_difference(even_set)

    result = ", ".join(map(str, final_set))
    print(result)

solve_names_ascii()
