lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_cost = 0
helmet_broken_count = 0
sword_broken_count = 0
shield_broken_count = 0
armor_broken_count = 0
count_of_helmets_and_swords = 1

for lost_game in range(1, lost_fights + 1):
    if lost_game % 2 == 0:
        helmet_broken_count += 1

    if lost_game % 3 == 0:
        sword_broken_count += 1
    if lost_game % 6 == 0:
        shield_broken_count += 1
        if shield_broken_count % 2 == 0:
            armor_broken_count += 1

total_cost = (helmet_price * helmet_broken_count) + (shield_price * shield_broken_count) + (sword_price * sword_broken_count) + (armor_broken_count * armor_price)
print(f"Gladiator expenses: {total_cost:.2f} aureus")
