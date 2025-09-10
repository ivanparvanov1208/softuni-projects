string = input()

while True:
    entry = input()
    if entry == "Done":
        break

    command_parts = entry.split()
    action = command_parts[0]

    if action == "Change":
        char = command_parts[1]
        replacement = command_parts[2]
        string = string.replace(char, replacement)
        print(string)

    elif action == "Includes":
        substring = command_parts[1]
        print("True" if substring in string else "False")

    elif action == "End":
        substring = command_parts[1]
        print("True" if string.endswith(substring) else "False")

    elif action == "Uppercase":
        string = string.upper()
        print(string)

    elif action == "FindIndex":
        char = command_parts[1]
        print(string.find(char))

    elif action == "Cut":
        start_index = int(command_parts[1])
        count = int(command_parts[2])
        string = string[start_index:start_index + count]
        print(string)
