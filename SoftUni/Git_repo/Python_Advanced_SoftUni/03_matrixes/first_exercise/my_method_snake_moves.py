r,c = [int(x) for x in input().split()]
txt = input()
matrix = []
full_txt = txt * r*2
end_index = c
curr_index = 0
for i in range(r):
    matrix.append(full_txt[curr_index:end_index])
    curr_index += c
    end_index += c
    if i % 2 != 0:
        matrix[i] = matrix[i][::-1]
[print(*row, sep="") for row in matrix]