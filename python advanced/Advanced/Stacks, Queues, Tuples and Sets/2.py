math_operators = ["+", "-", "*", "/"]

cmd_line = input().split()

firstEval = True

previousResult = 0

for i in range(len(cmd_line)):
    if cmd_line[i] in math_operators:
        if cmd_line[i] == "+":
            if firstEval:
                previousResult = int(cmd_line[i-1]) + int(cmd_line[i-2])
                firstEval = False
            elif not firstEval:
                if int(cmd_line[i - 2] == (x for x in math_operators)):
                    previousResult = previousResult + int(cmd_line[i - 1])
                else:
                    previousResult = previousResult + int(cmd_line[i - 1]) + int(cmd_line[i - 2])
        elif cmd_line[i] == "-":
            if firstEval:
                previousResult = int(cmd_line[i-1]) - int(cmd_line[i-2])
                firstEval = False
            elif not firstEval:
                if int(cmd_line[i - 2] == (x for x in math_operators)):
                    previousResult = previousResult - int(cmd_line[i - 1])
                else:
                    previousResult = previousResult - int(cmd_line[i - 1]) - int(cmd_line[i - 2])
        elif cmd_line[i] == "*":
            if firstEval:
                previousResult = int(cmd_line[i-1]) * int(cmd_line[i-2])
                firstEval = False
            elif not firstEval:
                if int(cmd_line[i - 2] == (x for x in math_operators)):
                    previousResult = previousResult * int(cmd_line[i - 1])
                else:
                    previousResult = previousResult * int(cmd_line[i - 1]) * int(cmd_line[i - 2])
        elif cmd_line[i] == "/":
            if firstEval:
                previousResult = int(cmd_line[i-1]) / int(cmd_line[i-2])
                firstEval = False
            elif not firstEval:
                if int(cmd_line[i-2] == (x for x in math_operators)):
                    previousResult = previousResult / int(cmd_line[i-1])
                else:
                    previousResult = previousResult / int(cmd_line[i - 1]) / int(cmd_line[i - 2])

print(previousResult)