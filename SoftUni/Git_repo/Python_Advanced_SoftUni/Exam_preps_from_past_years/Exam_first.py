from collections import deque

mechanical_parts = [int(x) for x in input().split()]
energy_level = deque(int(item) for item in input().split())
drones_built = []

types_of_drones = {
    100: "Sentinel-X",
    85: "Viper-MKII",
    75: "Aegis-7",
    65: "Striker-R",
    55: "Titan-Core"
}

while energy_level and mechanical_parts and len(drones_built) < 5:
    current_energy = energy_level[0]
    current_mech_parts = mechanical_parts[-1]
    total_power = current_energy + current_mech_parts

    built = False


    for required_power, drone_name in sorted(types_of_drones.items(), reverse=True):
        if total_power == required_power and drone_name not in drones_built:
            drones_built.append(drone_name)
            energy_level.popleft()
            mechanical_parts.pop()
            built = True
            break

    if not built:
        for required_power, drone_name in sorted(types_of_drones.items(), reverse=True):
            if total_power > required_power and drone_name not in drones_built:
                drones_built.append(drone_name)
                mechanical_parts.pop()
                reduced_energy = energy_level.popleft() - 30
                if reduced_energy > 0:
                    energy_level.append(reduced_energy)
                built = True
                break

    if not built:
        mechanical_parts.pop()
        reduced_energy = energy_level.popleft() -1
        if reduced_energy > 0:
            energy_level.append(reduced_energy)


if len(drones_built) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if drones_built:
    print("Assembled Drones: " + ', '.join(drones_built))

if mechanical_parts:
    print("Mechanical Parts:", end=' ')
    print(", ".join(str(mechanical_parts[x]) for x in range(len(mechanical_parts)-1,-1,-1)))

if energy_level:
    print("Power Cells:", ', '.join(str(x) for x in energy_level))
