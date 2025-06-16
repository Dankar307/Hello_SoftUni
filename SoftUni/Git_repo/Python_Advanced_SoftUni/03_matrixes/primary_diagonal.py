N = int(input())
matrix = []
sum_of_diagonal = 0
for num in range(N):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)
    sum_of_diagonal += matrix[num][num]
print(sum_of_diagonal)


