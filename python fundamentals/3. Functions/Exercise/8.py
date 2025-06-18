def is_palindrome(value: int):
    if value == int(str(value)[::-1]):
        return True
    else:
        return False

nums = input().split(", ")

list_to_alter = []

for num in nums:
    list_to_alter.append(int(num))

for i in range(len(list_to_alter)):
    print(is_palindrome(list_to_alter[i]))