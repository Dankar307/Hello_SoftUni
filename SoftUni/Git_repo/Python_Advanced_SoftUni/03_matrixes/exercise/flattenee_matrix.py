string_ = input().split("|")

matrix = []
for i in range(len(string_) -1, -1, -1):
    row = string_[i].split()
    if row:
        matrix.append(row)
for row in matrix:
    print(*row, end=" ")