r,c = [int(x) for x in input().split(", ")]
matrix = []
ct = [0,0]
TIME = 16
for i in range(r):
    matrix.append(list(input()))
    for j in range(c):
        if matrix[i][j] == "C":
            ct = [i,j]
            matrix[i][j] = "*"

moves = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
command = input()
while True:
    current_row = ct[0]
    current_col = ct[1]
    if command in moves:
        next_row = current_row + moves[command][0]
        next_col = current_col + moves[command][1]
        if 0<= next_row < r and 0<= next_col < c:
            next_position_element = matrix[next_row][next_col]
            ct = [next_row, next_col]

            if next_position_element == "T":
                matrix[next_row][next_col] = "*"
                TIME -=1
                print("Terrorists win!")
                [print(*row) for row in matrix]
                exit()
            elif next_position_element == "*":
                TIME -=1
                matrix[next_row][next_col] = "C"
        else:
            next_row = current_row
            next_col = current_col
            ct = [next_row, next_col]
            matrix[next_row][next_col] = "C"
            TIME -=1
        if TIME <= 0:
            break
    elif command == "defuse":
        next_position_element = matrix[current_row][current_col]
        if next_position_element == "B":
            TIME -= 4
            if TIME >= 0:
                matrix[current_row][current_col] = "D"
                break
            else:
                matrix[current_row][current_col] = "X"
                break

        else:
            TIME -= 2


    command = input()
if TIME <= 0:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(16 - TIME)+1} second/s.")
else:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {TIME} second/s remaining.")
[print(*row) for row in matrix]