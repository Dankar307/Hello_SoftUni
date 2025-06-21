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


while True:
    command = input()
    if command == "Christmas morning":
        matrix[santa[0]][santa[1]] = "S"
        break

    if num_presents == 0:
        print("Santa ran out of presents!")

        break

    move = command
    row = santa[0] + directions[move][0]
    column = santa[1] + directions[move][1]

    if 0 <= row < SIZE and 0 <= column < SIZE:
        santa = [row,column]


        if matrix[row][column] == "V":
            if num_presents > 0:

                matrix[santa[0]][santa[1]] = "S"
                num_presents -= 1
                good_kids_gifted += 1
                matrix[row][column] = "-"
            else:
                print("Santa ran out of presents!")
                matrix[santa[0]][santa[1]] = "S"
                [print(*row) for row in matrix]
                print(f"No presents for {abs(good_kids_gifted - good_kids)} nice kid/s.")
                exit()
        elif matrix[row][column] == "C":

            santa = [row, column]
            matrix[santa[0]][santa[1]] = "S"

            for direction in directions:
                row = santa[0] + directions[direction][0]
                column = santa[1] + directions[direction][1]
                if 0 <= row < SIZE and 0 <= column < SIZE:
                    if matrix[row][column] in "VX":

                        if num_presents > 0:
                            num_presents -= 1
                        if matrix[row][column] == "V":
                            good_kids_gifted += 1
                        matrix[row][column] = "-"
                        if num_presents ==0:
                            print("Santa ran out of presents!")
                            matrix[santa[0]][santa[1]] = "S"
                            [print(*row) for row in matrix]
                            print(f"No presents for {abs(good_kids_gifted-good_kids)} nice kid/s.")
                            exit()


    
    matrix[santa[0]][santa[1]] = "-"








if good_kids == good_kids_gifted:

    [print(*row) for row in matrix]
    print(f"Good job, Santa! {good_kids} happy nice kid/s.")
