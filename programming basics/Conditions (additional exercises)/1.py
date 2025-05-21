V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

workOfFirstPipe = P1 * H
workOfSecondPipe = P2 * H

workOfBothPipes = workOfFirstPipe + workOfSecondPipe

percentOfAll = (workOfBothPipes / V) * 100

percentOfFirst = (workOfFirstPipe / workOfBothPipes) * 100

percentOfSecond = (workOfSecondPipe / workOfBothPipes) * 100

if workOfBothPipes < V:
    print(f"The pool is {percentOfAll}% full. Pipe 1: {percentOfFirst}%. Pipe 2: {percentOfSecond}%.")
else:
    excessWater = workOfBothPipes - V
    print(f"For {H} hours the pool overflows with {excessWater} liters.")