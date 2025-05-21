graders = int(input())

allGradesSum = 0
presentations = 0

while True:
    is_number = False
    command = input()

    num1, num2 = "", ""

    for index, digit in enumerate(command):
        if digit == ".":
            num1, num2 = command.split(".")
            break

    if num1.isdigit() and num2.isdigit():
        is_number = True
    elif command == "Finish":
        break
    else:
        presentation = command

        gradeSum = 0

        for i in range(graders):
            grade = float(input())
            gradeSum += grade

        average = gradeSum / graders

        allGradesSum += average

        presentations += 1

        print(f"{presentation} - {average:.2f}.")

averageAll = allGradesSum / presentations

print(f"Student's final assessment is {averageAll:.2f}.")