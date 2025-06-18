def validating_input(row, col, rows, cols):
    if row in range(rows) and col in range(cols):
        return True


r,c = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(r)]
line = input()
while line != "END":
    command = line.split()
    if command[0] == "swap" and len(command) == 5:
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if validating_input(row1, col1, r, c) and validating_input(row2, col2, r, c):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    line = input()