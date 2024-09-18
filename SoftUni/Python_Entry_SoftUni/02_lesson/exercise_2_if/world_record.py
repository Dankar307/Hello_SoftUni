from math import floor
world_record = float(input())
distance = float(input())
time_for_1_meter = float(input())

time_for_finishing = distance * time_for_1_meter

delay = floor(distance / 15) * 12.5

whole_time = time_for_finishing + delay

time_needed = abs(world_record - whole_time)

if world_record > whole_time:
    print(f"Yes, he succeeded! The new world record is {whole_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")
