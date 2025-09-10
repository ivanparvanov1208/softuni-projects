capacity = int(input())
users = {}

while True:
    command = input()
    if command == "Statistics":
        break

    command_parts = command.split("=")
    action = command_parts[0]

    if action == "Add":
        username = command_parts[1]
        sent = int(command_parts[2])
        received = int(command_parts[3])
        if username not in users:
            users[username] = [sent, received]

    elif action == "Message":
        sender = command_parts[1]
        receiver = command_parts[2]
        if sender in users and receiver in users:
            users[sender][0] += 1
            users[receiver][1] += 1

            if users[sender][0] + users[sender][1] >= capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]

            if users[receiver][0] + users[receiver][1] >= capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]

    elif action == "Empty":
        username = command_parts[1]
        if username == "All":
            users.clear()
        elif username in users:
            del users[username]

print(f"Users count: {len(users)}")
for username, (sent, received) in users.items():
    total_messages = sent + received
    print(f"{username} - {total_messages}")
