def min_max_sum(nums = input().split(" ")):
    list_to_alter = []
    for num in nums:
        list_to_alter.append(int(num))

    min_num = min(list_to_alter)
    max_num = max(list_to_alter)
    return print(f"The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum(list_to_alter)}")

min_max_sum()