N = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(N)]
primary_diagonal = [matrix[i][i] for i in range(N)]
secondary_diagonal = [matrix[i][-1-i] for i in range(N)]
primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)
difference = abs(primary_sum - secondary_sum)
print(f"{difference}")