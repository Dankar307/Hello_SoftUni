num = int(input())
sum_of_nums = int(input())
while sum_of_nums != num:
    if sum_of_nums <= num:

        sum_of_nums += int(input())
    else:
        break
print(sum_of_nums)

