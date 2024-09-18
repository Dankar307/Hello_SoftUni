from math import floor
num_of_matches = int(input())
points_at_the_start_of_the_season = int(input())
win_counter = 0
sum_of_points = points_at_the_start_of_the_season
for _ in range(num_of_matches):
    match_state = input()
    if match_state == 'W':
        win_counter += 1
        sum_of_points += 2000
    elif match_state == 'F':
        sum_of_points += 1200
    elif match_state == 'SF':
        sum_of_points += 720

average_points = (sum_of_points - points_at_the_start_of_the_season) / num_of_matches
win_percentage = (win_counter / num_of_matches) * 100
print(f"Final points: {sum_of_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_percentage:.2f}%")