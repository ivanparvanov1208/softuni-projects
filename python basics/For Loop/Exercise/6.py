actorName = input()
points = float(input())
gradersCount = int(input())

for i in range(gradersCount):
    graderName = input()
    grade = float(input())

    points = points + ((len(graderName) * grade) / 2)

    if points >= 1250.5:
        print(f"Congratulations, {actorName} got a nominee for leading role with {points}!")
        break


if points <= 1250.5:
    diff = 1250.5 - points

    print(f"Sorry, {actorName} you need {diff:.1f} more!")

