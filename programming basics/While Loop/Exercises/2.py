displeasingGradesInput = int(input())
displeasingGrades = 0
problems = 0
sum = 0

lastProblem = ""

while True:
    command = input()
    if command != "Enough":
        grade = int(input())
        if grade > 4:
            problems += 1
            sum += grade
            lastProblem = command
            continue
        else:
            displeasingGrades += 1
            if displeasingGrades == displeasingGradesInput:
                print(f"You need a break, {displeasingGrades} poor grades.")
                break
            problems += 1
            sum += grade
            lastProblem = command

    else:
        average = sum / problems
        print(f"Average score: {average:.2f}\nNumber of problems: {problems}\nLast problem: {lastProblem}")
        break
