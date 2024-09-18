n = int(input())
left_side_sum = 0
right_side_sum = 0
for numbers in range(2 * n):
    if numbers < n:
        left_side_sum = left_side_sum + int(input())
    else:
        right_side_sum = right_side_sum + int(input())

if left_side_sum == right_side_sum:
    print(f"Yes, sum = {left_side_sum}")
else:
    difference = abs(left_side_sum - right_side_sum)
    print(f"No, diff = {difference}")
