direction_mapper = {"up": (-1,0),"down": (1,0),"left": (0,-1),"right": (0,1)}


def Calculate_move(curren_row,curren_col,direction, size):

    new_row = (curren_row + direction_mapper[direction][0]) % size
    new_col = (curren_col + direction_mapper[direction][1]) % size
    return new_row, new_col




SIZE = int(input())
matrix = []
ship = [0,0]
durability = 100
is_charmed = False
tressure_count = 0
for i in range(SIZE):
    matrix.append(list(input()))
    for j in range(SIZE):
        if matrix[i][j] == "S":
            ship = [i,j]
            matrix[i][j] = "."
        elif matrix[i][j] == "*":
            tressure_count += 1






command = input()
while command != "stop":
    current_row = ship[0]
    current_col = ship[1]
    matrix[ship[0]][ship[1]] = "."
    move = command
    next_row,next_col = Calculate_move(current_row,current_col,move,SIZE)

    if matrix[next_row][next_col] == ".":

        ship = [next_row,next_col]
        matrix[ship[0]][ship[1]] = "S"
    elif matrix[next_row][next_col] == "*":
        matrix[ship[0]][ship[1]] = "."
        tressure_count -= 1
        ship = [next_row,next_col]
        matrix[ship[0]][ship[1]] = "."
        if tressure_count == 0:
            print(f"Yo-ho-ho! All treasure chests collected!")
            break

    elif matrix[next_row][next_col] == "C" and not is_charmed:
        matrix[ship[0]][ship[1]] = "."
        ship = [next_row, next_col]
        matrix[ship[0]][ship[1]] = "."
        is_charmed = True
        if durability + 25 > 100:
            durability = 100
        else:
            durability += 25
    elif matrix[next_row][next_col] == "C" and is_charmed:
        matrix[ship[0]][ship[1]] = "."
        ship = [next_row, next_col]
        matrix[ship[0]][ship[1]] = "."

    elif matrix[next_row][next_col] == "M":
        durability -= 25
        matrix[ship[0]][ship[1]] = "."
        ship = [next_row, next_col]
        if durability == 0:
            print(f"Shipwreck! Last known coordinates ({ship[0]}, {ship[1]})")
            break
    command = input()
if command == "stop" and tressure_count > 0:
    print(f"Retreat! Some treasures remain unclaimed.")

print(f"Ship Durability: {durability}")
if tressure_count > 0:
    print(f"Unclaimed chests: {tressure_count}")
matrix[ship[0]][ship[1]] = "S"
for row in matrix:
    print("".join(str(x)for x in row))
