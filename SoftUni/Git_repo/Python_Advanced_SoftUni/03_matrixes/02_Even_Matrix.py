N = int(input())
matrix = []
for rows in range(N):
    matrix.append([int(i) for i in input().split(", ") if int(i) % 2 == 0])
print(matrix)