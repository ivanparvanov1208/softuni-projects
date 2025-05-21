username = input()
password = input()

while True:
    data = input()
    if data != password:
        continue
    else:
        print(f"Welcome {username}!")
        break