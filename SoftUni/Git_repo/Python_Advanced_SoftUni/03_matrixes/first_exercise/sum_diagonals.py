N = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(N)]

primary_diagonal = [matrix[i][i] for i in range(N)]
secondary_diagonal = [matrix[i][-1-i] for i in range(N)]
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")