rows, columns = map(int, input().split())

matrix = [[] for _ in range(rows)]

count = 0

for i in range(rows):
    matrix[i] += input().split()

for row in range(rows - 1):
    for col in range(columns - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            count += 1

print(count)