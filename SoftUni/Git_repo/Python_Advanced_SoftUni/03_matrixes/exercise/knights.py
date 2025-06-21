rows = int(input())
knights = []
matrix = []
for row in range(rows):
    matrix.append(list(input()))
    for column in range(rows):
        if matrix[row][column] == "K":
            knights.append((row, column))
removed_knights = 0
possible_moves = [(1,2), (2,1),(-1,-2),(-2,-1),(1,-2),(-1,2),(-2,1),(2,-1)]
while True:

    max_knight = [0,0]
    max_hits = 0

    for row,col in knights:
        hits = 0
        for move in possible_moves:

            next_row = row + move[0]
            next_column = col + move[1]
            if 0<= next_row < rows and 0 <= next_column < rows:

                if matrix[next_row][next_column] == "K":
                    hits+=1
        if hits > max_hits:

            max_hits = hits
            max_knight = [row,col]
    if max_hits == 0:
        break

    knights.remove(tuple(max_knight))

    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1
print(removed_knights)