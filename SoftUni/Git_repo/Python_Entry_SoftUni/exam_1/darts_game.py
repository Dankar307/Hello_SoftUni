player_name = input()
starting_points = 301
is_valid = True
count_shots = 0
avalabe_points = 301

unlucky_shot = 0
while True:
    pole = input()
    if pole != 'Retire':
        points = int(input())
        if pole == "Single":
            if starting_points >= points:
                count_shots += 1
                starting_points -= points
            else:
                unlucky_shot += 1
        elif pole == "Double":
            if starting_points >= points * 2:
                count_shots += 1
                starting_points -= points * 2
            else:
                unlucky_shot += 1
        elif pole == 'Triple':
            if starting_points >= points * 3:
                count_shots += 1
                starting_points -= points * 3
            else:
                unlucky_shot += 1
    else:
        is_valid = False
        break
    if starting_points == 0:
        break
if is_valid:
    print(f"{player_name} won the leg with {count_shots} shots.")

else:
    print(f"{player_name} retired after {unlucky_shot} unsuccessful shots.")