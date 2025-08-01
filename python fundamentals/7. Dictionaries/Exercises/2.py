resources = {}

while True:
    command = input()
    if command != "stop":
        quantity = int(input())
        if command not in resources:
            resources[command] = quantity
        else:
            resources[command] += quantity
    else:
        break

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")