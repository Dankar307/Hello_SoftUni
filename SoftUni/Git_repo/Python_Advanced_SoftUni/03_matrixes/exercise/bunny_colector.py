

n = int(input())
matrix = []
bunnie = [0, 0]
for i in range(n):
    matrix.append(list(input().split()))
    for j in range(n):
        if matrix[i][j] == "B":
            bunnie = [i, j]
max_eggs_collected = -float("inf")
max_path = []
max_direction = ''

opperator = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)

}

for direction, move in opperator.items():
    eggs = 0
    curr_egg_matrix = []
    row = bunnie[0] + move[0]
    col = bunnie[1] + move[1]
    while 0<=row<n and 0<=col<n:
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        curr_egg_matrix.append([row,col])
        row += move[0]
        col += move[1]
    if eggs > max_eggs_collected and curr_egg_matrix:
        max_eggs_collected = eggs
        max_path = curr_egg_matrix
        max_direction = direction
print(f"{max_direction}")
[print(x, sep="\n") for x in max_path]
print(f"{max_eggs_collected}")