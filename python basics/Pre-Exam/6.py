firstNumberBorder = int(input())
secondNumberBorder = int(input())
thirdNumberBorder = int(input())

for i in range(1, firstNumberBorder + 1):
    if i % 2 != 0:
        continue
    for j in range(1, secondNumberBorder + 1):
        if j not in [2, 3, 5, 7]:
            continue
        for k in range(1, thirdNumberBorder + 1):
            if k % 2 != 0:
                continue
            print(f"{i} {j} {k}")