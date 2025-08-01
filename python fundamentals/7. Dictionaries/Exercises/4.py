phoneBook = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    name, number = entry.split("-")
    phoneBook[name] = number

searches = int(entry)
for search in range(searches):
    searched_name = input()
    if searched_name in phoneBook.keys():
        print(f"{searched_name} -> {phoneBook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")