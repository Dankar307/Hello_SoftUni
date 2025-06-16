size,_ = input().split(", ")
matrix = []
sum_matrix = 0
for i in range(int(size)):
    row = [int(el) for el in input().split(", ")]
    sum_matrix += sum(row)
    matrix.append(list(row))
print(sum_matrix)
print(matrix)