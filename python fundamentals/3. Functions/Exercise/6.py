def sorted_list(nums = input().split(" ")):
    list_to_sort = []

    for num in nums:
        list_to_sort.append(int(num))

    return sorted(list_to_sort)

print(sorted_list())