factor = int(input())
count = int(input())

list = []

for i in range(count + 1):
    number = i * factor
    if number >= factor:
        list.append(number)

print(list)