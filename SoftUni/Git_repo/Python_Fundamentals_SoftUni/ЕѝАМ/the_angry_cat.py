price_rating_list = [int(num) for num in input().split(", ")]
entry_point = int(input())
item_type = input() # cheap or expensive
right_part = price_rating_list[entry_point+1:]
left_part = price_rating_list[:entry_point]

if item_type == "cheap":
    left_damage = sum(item for item in left_part if item < price_rating_list[entry_point])
    right_damage = sum(item for item in right_part if item < price_rating_list[entry_point])
else:
    left_damage = sum(item for item in left_part if item >= price_rating_list[entry_point])
    right_damage = sum(item for item in right_part if item >= price_rating_list[entry_point])


if left_damage >= right_damage:
    print(f"Left - {left_damage}")
else:
    print(f"Right - {right_damage}")
