import sys
from sys import maxsize
n = int(input())
sum_of_nums = int(input())
max_num = -sys.maxsize
for numbers in range(n):
    current_num = int(input())

    if max_num < current_num:
        max_num = current_num
    sum_of_nums += current_num


if max_num == sum_of_nums - max_num:
    print("Yes")
    print(f'Sum = {max_num}')
else:
    difference = abs(max_num - (sum_of_nums  - max_num))
    print(f'No')
    print(f'Diff = {difference}')