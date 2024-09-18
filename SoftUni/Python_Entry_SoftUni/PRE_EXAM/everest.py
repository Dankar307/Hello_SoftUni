base_camp_height = 5364
max_height = 8848
max_days = 5

total_height = base_camp_height
days = 0
night_before = input()
while night_before != 'End':
    if days > max_days or total_height >= max_height:
        break


    if night_before == "Yes":
        rest_height = int(input())
        total_height += rest_height
        days += 1
        if total_height >= max_height:
            break
    elif night_before == 'No':
        climb_height = int(input())
        total_height += climb_height

        if total_height >= max_height:
            break
        night_before = input()

if total_height >= max_height:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{total_height}")
