from collections import deque

r,c = [int(x) for x in input().split()]
snake = deque(input())
matrix = []
for row in range(r):
    matrix.append([''] * c)
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = snake[0]
        else:
            matrix[row][-1-col] = snake[0]
        snake.rotate(-1)
[print(*row, sep="") for row in matrix]