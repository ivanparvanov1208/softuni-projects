def check(list1, list2, newlist):
    for item in list1:
        for i in range(len(list2)):
            if item in list2[i] and item not in newlist:
                newlist.append(item)
    return newlist

list1 = input().split(", ")
list2 = input().split(", ")

newlist = []

print(check(list1, list2, newlist))