import os


while True:
    input_ = input()

    if input_ == "End":
        break

    command, filename, *args = input_.split("-")

    if command == 'Create':
        open(filename, 'w').close()

    elif command == "Add":
        with open(filename, 'a') as f:
            f.write(f"{args[0]}\n")

    elif command == "Replace":
        try:
            with open(filename, 'r+') as f:
                content = f.read()
                f.seek(0)
                f.truncate(0)
                f.write(content.replace(args[0], args[1]))
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("An error occurred")