favouriteBook = input()
searchedBooks = 0

while True:
    command = input()

    if command == favouriteBook:
        print(f"You checked {searchedBooks} books and found it.")
        break
    elif command == "No More Books" or command == "No More Books ":
        print(f"The book you search is not here!\nYou checked {searchedBooks} books.")
        break
    else:
        searchedBooks += 1