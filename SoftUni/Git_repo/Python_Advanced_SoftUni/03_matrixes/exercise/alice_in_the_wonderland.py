

n= int(input())
matrix = []
alice = []
for i in range(n):
    matrix.append(list(input().split()))
    for j in range(n):
        if matrix[i][j] == "A":
            alice = [i, j]
            matrix[i][j] = "*"



directions = {"up": (-1,0),"down": (1,0),"left": (0,-1),"right": (0,1)}
bags_of_tea = 0

while bags_of_tea < 10:
    command = input()


    row = alice[0] + directions[command][0]
    col = alice[1] + directions[command][1]
    if row < 0 or row >= n or col < 0 or col >= n:
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    if matrix[row][col] not in  "*.":
        bags_of_tea += int(matrix[row][col])
    matrix[row][col] = "*"
    alice = [row, col]
if bags_of_tea < 10:
    print("Alice didn't make it to the tea party.")

else:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]

