pour_count = int(input())
total_liters = 0

for i in range(0, pour_count):
    liters_of_water = int(input())
    if total_liters + liters_of_water > 255:
        print("Insufficient capacity!")
        continue
    else:
        total_liters += liters_of_water
print(f'{total_liters}')