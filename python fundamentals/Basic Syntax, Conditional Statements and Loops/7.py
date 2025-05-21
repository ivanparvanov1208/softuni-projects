while True:
    command = input()

    string = ""

    if command == "SoftUni":
        continue
    elif command == "End":
        break
    else:
        for letter in command:
            string = string + "".join(letter * 2)
        print(string)