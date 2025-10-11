n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primaryDiagonal = [matrix[i][i] for i in range(n)]
secondaryDiagonal = [matrix[i][-1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primaryDiagonal)}. Sum: {sum(primaryDiagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondaryDiagonal)}. Sum: {sum(secondaryDiagonal)}")