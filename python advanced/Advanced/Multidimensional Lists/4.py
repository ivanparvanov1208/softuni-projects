rows, columns = map(int, input().split())

matrix = [[] for _ in range(rows)]

for i in range(rows):
    matrix[i] += map(int, input().split())

Sum = 0

for row in range(rows - 2):
    for col in range(columns - 2):
        if Sum < matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]:
            newMatrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]], [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]], [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]
            Sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

print(f"Sum = {Sum}")
for j in range(3):
    print(" ".join(str(x) for x in newMatrix[j]))
