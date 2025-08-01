charCount = {}

string = input().split(" ")

for word in string:
    for char in word:
        if char not in charCount:
            charCount[char] = 1
        else:
            charCount[char] += 1

for char, count in charCount.items():
    print(f"{char} -> {count}")