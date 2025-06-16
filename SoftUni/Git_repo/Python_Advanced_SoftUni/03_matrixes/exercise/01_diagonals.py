N = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
sum_of_prime = []

for _ in range(N):
    row_data = input().split(", ")
    matrix.append(row_data)


primary_diagonal= [str(matrix[i][i] for i in range(N))]
secondary_diagonal.append(str(matrix[-i][-i] for i in range(N)))
sum_of_prime.append(int(num) for num in primary_diagonal)
sum_of_prime.append(int(num) for num in secondary_diagonal)
print(f"Primary diagonal: { ", ".join(primary_diagonal) }. Sum: {sum_of_prime[0]}\nSecondary diagonal: { ", ".join(primary_diagonal) }. Sum: {sum_of_prime[1]}")