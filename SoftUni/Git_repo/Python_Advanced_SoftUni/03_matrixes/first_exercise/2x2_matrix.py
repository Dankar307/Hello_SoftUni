

row,col = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(row)]
count_of_occurrences = 0
for rows in range(row-1):
    for column in range(col-1):

        if matrix[rows][column] == matrix[rows+1][column] == matrix[rows+1][column+1] == matrix[rows][column+1]:
            count_of_occurrences += 1


print(count_of_occurrences)