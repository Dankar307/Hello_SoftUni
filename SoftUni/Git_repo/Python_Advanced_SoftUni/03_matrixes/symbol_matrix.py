N = int(input())
matrix = []

for _ in range(N):
    row_data = [el for el in input()]
    matrix.append(row_data)

item_for_search = input()
for row in range(len(matrix)):
    if item_for_search in matrix[row]:
        index = matrix[row].index(item_for_search)
        print(f"({row}, {index})")
        exit()
print(f"{item_for_search} does not occur in the matrix")
