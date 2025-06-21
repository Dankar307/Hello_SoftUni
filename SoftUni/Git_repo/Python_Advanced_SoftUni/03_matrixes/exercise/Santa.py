num_presents = int(input())
SIZE = int(input())
matrix = []
santa = [0,0]
good_kids = 0
good_kids_gifted = 0
directions = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}
for i in range(SIZE):
    matrix.append(input().split())
    for j in range(SIZE):
        if matrix[i][j] == "S":
            santa = [i,j]
            matrix[i][j] = "-"
        elif matrix[i][j] == "V":
            good_kids += 1

command = input()
while True:

    if command == "Christmas morning":
        matrix[santa[0]][santa[1]] = "S"
        break

    if num_presents == 0:
        print("Santa ran out of presents!")

        break

    move = command
    row = santa[0] + directions[move][0]
    column = santa[1] + directions[move][1]

    if 0 <= row < SIZE and 0 <= column < SIZE and num_presents !=0:
        santa = [row,column]


        if matrix[row][column] == "V":
            matrix[santa[0]][santa[1]] = "S"
            num_presents -= 1
            good_kids_gifted += 1
            matrix[row][column] = "-"

        elif matrix[row][column] == "C":

            santa = [row, column]
            matrix[santa[0]][santa[1]] = "S"

            for direction in directions:
                row = santa[0] + directions[direction][0]
                column = santa[1] + directions[direction][1]


                if 0 <= row < SIZE and 0 <= column < SIZE and num_presents > 0:
                    santa = [row, column]


                    if matrix[row][column] in "VX":
                        num_presents -= 1
                        matrix[row][column] = "-"


                        if matrix[row][column] == "V":
                            if num_presents > 0:
                                good_kids_gifted += 1
                            matrix[row][column] = "-"

                if num_presents <= 0:
                    print("Santa ran out of presents!")
                    matrix[santa[0]][santa[1]] = "S"
                    [print(*row) for row in matrix]
                    print("No presents for {count nice kids} nice kid/s.")
                    exit()
    else:
        print("Santa ran out of presents!")
        matrix[santa[0]][santa[1]] = "S"
        [print(*row) for row in matrix]
        break
    matrix[santa[0]][santa[1]] = "-"
    command = input()







if good_kids == good_kids_gifted:
    print(f"Good job, Santa! {good_kids} happy nice kid/s.")

    [print(*row) for row in matrix]
