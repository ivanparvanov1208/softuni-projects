usernames = ()
n = int(input())

for i in range(n):
    username = input()

    if username not in usernames:
        listUsernames = list(usernames)
        listUsernames.append(username)
        usernames = tuple(listUsernames)


for username in usernames:
    print(username)