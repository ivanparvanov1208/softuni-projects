directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

n = int(input())
grid = [list(input()) for _ in range(n)]

pacman_pos = None
for r in range(n):
    for c in range(n):
        if grid[r][c] == 'P':
            pacman_pos = (r, c)
            break
    if pacman_pos:
        break

total_stars = sum(cell == '*' for row in grid for cell in row)
collected_stars = 0
health = 100
immunity = False
game_over = False
win = False

while True:
    command = input()
    if command == "end":
        break

    dr, dc = directions[command]
    r, c = pacman_pos
    new_r = (r + dr) % n
    new_c = (c + dc) % n
    cell = grid[new_r][new_c]

    grid[r][c] = '-'

    if cell == '*':
        collected_stars += 1
    elif cell == 'G':
        if not immunity:
            health -= 50
            if health <= 0:
                game_over = True
        else:
            immunity = False
    elif cell == 'F':
        immunity = True

    grid[new_r][new_c] = 'P'
    pacman_pos = (new_r, new_c)

    if collected_stars == total_stars:
        win = True
        break
    if game_over:
        break

if game_over:
    print(f"Game over! Pacman last coordinates [{pacman_pos[0]},{pacman_pos[1]}]")
elif win:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")
if collected_stars < total_stars:
    print(f"Uncollected stars: {total_stars - collected_stars}")

for row in grid:
    print(''.join(row))

