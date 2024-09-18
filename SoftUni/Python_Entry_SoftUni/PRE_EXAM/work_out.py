from math import ceil
N = int(input())
M = int(input())
total_distance = M
for _ in range(N):
    percentage_increase = int(input()) / 100
    M += M * percentage_increase
    total_distance += M
if total_distance >= 1000:
    print(f"You've done a great job running {ceil(total_distance - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(abs(total_distance - 1000))} more kilometers")
