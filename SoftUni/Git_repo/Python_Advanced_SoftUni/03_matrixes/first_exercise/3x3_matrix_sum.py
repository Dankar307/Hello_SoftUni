

r,c = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(r)]
start_index = 0
end_index = 0
curr_sum = 0
max_sum = -float('inf')
for rows in range(r-2):
    for columns in range(c-2):
        curr_sum = 0
        for i in range(rows, rows + 3):
            for j in range(columns, columns + 3):
                curr_sum += matrix[i][j]
                if curr_sum > max_sum:
                    start_index = rows
                    end_index = columns
                    max_sum = curr_sum
print(f"Sum = {max_sum}")
max_matrix = [matrix[r][end_index:end_index+3] for r in range(start_index, start_index+3)]
for i in max_matrix:
    print(*i)