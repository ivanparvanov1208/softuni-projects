def return_the_smallest():
    nums = []
    for i in range(3):
        nums.append(int(input()))
    return min(nums)

print(return_the_smallest())