n = int(input())

p1count = 0
p2count = 0
p3count = 0
p4count = 0
p5count = 0

if 1 <= n <= 1000:
    for i in range(n):
        num = int(input())

        if num < 200:
            p1count += 1
        elif 200 <= num <= 399:
            p2count += 1
        elif 400 <= num <= 599:
            p3count += 1
        elif 600 <= num <= 799:
            p4count += 1
        if num >= 800:
            p5count += 1

    p1 = p1count / n * 100
    p2 = p2count / n * 100
    p3 = p3count / n * 100
    p4 = p4count / n * 100
    p5 = p5count / n * 100

    print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")