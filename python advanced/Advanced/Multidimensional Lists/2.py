n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primaryDiagonal = [matrix[i][i] for i in range(n)]
secondaryDiagonal = [matrix[i][-1-i] for i in range(n)]

primarySum = sum(primaryDiagonal)
secondarySum = sum(secondaryDiagonal)

result = primarySum - secondarySum

print(abs(result))