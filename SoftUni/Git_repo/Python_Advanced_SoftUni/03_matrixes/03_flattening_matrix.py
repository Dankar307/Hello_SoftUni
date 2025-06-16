N = int(input())
matrix = []
flattered_list = []
for row in range(N):
   matrix.append(list(int(num) for num in input().split(", ")))
for lists in range(len(matrix)):
   for items in matrix[lists]:
      flattered_list.append(items)
print(flattered_list)