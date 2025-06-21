def Bunnies_expantion(matrix, bunnies):
    new_bunnies = set()
    bunnies_moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for b_row,b_col in bunnies:
        for d_row,d_col in bunnies_moves:
            new_row = b_row + d_row
            new_col = b_col + d_col
            if new_row in range(len(matrix)) and new_col in range(len(matrix[0])) :
                matrix[new_row][new_col] = "B"
                new_bunnies.add((new_row,new_col))



    return matrix, bunnies.union(new_bunnies)



row, col = [int(x) for x in input().split()]
matrix = []
p_row,p_col = 0,0
bunnies = set()
for r in range(row):
    matrix.append(list(input()))
    for c in range(col):
        if matrix[r][c] == 'B':
            bunnies.add((r,c))
        if matrix[r][c] == 'P':
            p_row,p_col = r,c
commands = list(input())


has_won = False
has_lost = False

moves = {
    "U": lambda r, c: (r-1, c),
    "D":lambda r, c: (r+1, c),
    "L":lambda r, c: (r, c-1),
    "R":lambda r, c: (r, c+1)
}

for command in commands:
    new_row,new_col = moves[command](p_row,p_col)
    matrix, bunnies = Bunnies_expantion(matrix, bunnies)
    if (p_row, p_col) not in bunnies:

        matrix[p_row][p_col] = '.'
    if new_row not in range(len(matrix)) or new_col not in range(len(matrix[0])):
        has_won = True
        break
    p_row, p_col = new_row, new_col
    if matrix[p_row][p_col] == "B":
        has_lost = True
        break



[print(*row, sep="") for row in matrix]
if has_won:
    print(f"won: {' '.join(str(x) for x in (p_row,p_col))}")
else:
    print(f"dead: {' '.join(str(x) for x in (p_row,p_col))}")