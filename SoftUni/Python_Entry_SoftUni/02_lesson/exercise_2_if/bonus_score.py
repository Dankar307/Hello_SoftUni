points = int(input())

bonus_points = 0

if points <= 100:
    bonus_points = 5
elif points >100 and points < 1000:
    bonus_points = points * 0.2
else:
    bonus_points = points * 0.1

second_bonus = 0

if points % 2 == 0:
    second_bonus = 1
elif points % 10 == 5:
    second_bonus = 2

final_bonus = bonus_points + second_bonus
final_points = final_bonus + points
print(final_bonus)
print(final_points)
