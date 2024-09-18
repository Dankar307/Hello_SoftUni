all_nums = int(input())
points_1 = 0
points_2 = 0
points_3 = 0
points_4 = 0
points_5 = 0

for numbers in range(0, all_nums):
    current_num = int(input())
    if current_num < 200:
        points_1 = points_1 + 1
    elif 200 <= current_num <= 399:
        points_2 = points_2 + 1
    elif 400 <= current_num <= 599:
        points_3 = points_3 + 1
    elif 600 <= current_num <= 799:
        points_4 = points_4 + 1
    elif current_num >= 800:
        points_5 = points_5 + 1

p1 = (points_1 / all_nums) * 100
p2 = (points_2 / all_nums) * 100
p3 = (points_3 / all_nums) * 100
p4 = (points_4 / all_nums) * 100
p5 = (points_5 / all_nums) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')