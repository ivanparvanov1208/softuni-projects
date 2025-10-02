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
            if not firstEval:
                previousResult = previousResult + int(cmd_line[i-1]) + int(cmd_line[i-2])
        if cmd_line[i] == "-":
            if firstEval:
                previousResult = int(cmd_line[i-1]) - int(cmd_line[i-2])
                firstEval = False
            if not firstEval:
                previousResult = previousResult - int(cmd_line[i-1]) - int(cmd_line[i-2])
        if cmd_line[i] == "*":
            if firstEval:
                previousResult = int(cmd_line[i-1]) * int(cmd_line[i-2])
                firstEval = False
            if not firstEval:
                previousResult = previousResult * int(cmd_line[i-1]) * int(cmd_line[i-2])
        if cmd_line[i] == "/":
            if firstEval:
                previousResult = int(cmd_line[i-1]) / int(cmd_line[i-2])
                firstEval = False
            if not firstEval:
                previousResult = previousResult / int(cmd_line[i-1]) / int(cmd_line[i-2])

print(previousResult)