coffees = 0

while True:
    event = input()

    if event == "END":
        break
    elif event.lower() in ["coding", "dog", "cat", "movie"]:
        if event.isupper():
            coffees += 2
        elif event.islower():
            coffees += 1
        else:
            coffees += 1  # Optional: Handle mixed case as 1 coffee

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)