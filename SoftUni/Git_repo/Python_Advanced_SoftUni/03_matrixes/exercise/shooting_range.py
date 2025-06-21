rows, cols = 5,5
matrix = []
my_position = []
targets = 0
directions = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}
targets_hit = 0
targets_hit_position = []

for row in range(rows):
    matrix.append(list(input().split()))

    for col in range(cols):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

number_of_commands = int(input())
for _ in range(number_of_commands):
    commands = input().split()
    if commands[0] == "move":


        move = directions[commands[1]]
        row = my_position[0]+ move[0]  *  int(commands[2])
        col = my_position[1]+ move[1]  *  int(commands[2])
        if 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == ".":
            my_position = [row, col]
            matrix[row][col] = "A"


    elif commands[0] == "shoot":
        direction = directions[commands[1]]
        row = direction[0] + my_position[0]
        col = direction[1] + my_position[1]
        for i in range(5):

            if 0<= row < 5 and 0<= col < 5:
                if matrix[row][col] == "x":
                    targets_hit += 1
                    targets -= 1
                    targets_hit_position.append([row, col])
                    break

                row += direction[0]
                col += direction[1]
        if not targets:
            print(f"Training completed! All {targets_hit} targets hit.")
            break
if targets:
    print(f"Training not completed! {targets} targets left.")


[print(row, sep="\n") for row in targets_hit_position]
