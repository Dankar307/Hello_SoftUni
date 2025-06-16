N = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(N)]

while True:
    command = input()
    if command == "END":
        break
    _, row, column, value = command.split()
    if int(row) not in range(0,len(matrix)) or int(column) not in range(0,len(matrix)):
        print("Invalid coordinates")
        continue
    else:
        if command.startswith("Add"):

            matrix[int(row)][int(column)] += int(value)
        elif command.startswith("Subtract"):

            matrix[int(row)][int(column)] -= int(value)



for row in matrix:
    print(*row)