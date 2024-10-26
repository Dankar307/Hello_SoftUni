number_of_days_adventure = int(input())
number_of_participants = int(input())
groups_energy = float(input())
water_per_person = float(input())
food_per_person = float(input())
total_water = water_per_person * number_of_participants * number_of_days_adventure
total_food = food_per_person * number_of_participants * number_of_days_adventure
for day in range(1, number_of_days_adventure + 1):
    energy_lost_for_the_day = float(input())
    groups_energy -= energy_lost_for_the_day
    if groups_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        exit()
    if day % 2 == 0:
        groups_energy += groups_energy * 0.05
        total_water -= total_water * 0.3
    if day % 3 == 0:
        groups_energy += groups_energy * 0.1
        total_food -= (total_food / number_of_participants)
print(f"You are ready for the quest. You will be left with {groups_energy:.2f} energy!")