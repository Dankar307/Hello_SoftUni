pirate_ship_status = [int(num) for num in input().split(">")]
warship_ship_status = [int(num) for num in input().split(">")]
max_section_health = int(input())
repair_sections_count = 0
while True:
    command = input()
    if command != "Retire":
        commands = command.split()
        if commands[0] == "Fire":
            damage = int(commands[2])
            index = int(commands[1])
            if index in range(len(warship_ship_status)):
                warship_ship_status[index] -= damage
                if warship_ship_status[index] < 0:
                    print("You won! The enemy ship has sunken.")
                    exit()
            else:
                continue
        if commands[0] == "Defend":
            start_index = int(commands[1])
            ending_index = int(commands[2])
            damage = int(commands[3])

            if start_index in range(len(pirate_ship_status)) and ending_index in range(len(pirate_ship_status)):
                for attacks in range(start_index,ending_index + 1):
                    pirate_ship_status[attacks] -= damage
                    if pirate_ship_status[attacks] < 0:
                        print("You lost! The pirate ship has sunken.")
                        exit()
            else:
                continue
        if commands[0] == "Repair":
            index = int(commands[1])
            health = int(commands[2])
            if index in range(len(pirate_ship_status)):
                pirate_ship_status[index] += health
                if pirate_ship_status[index] > max_section_health:
                    pirate_ship_status[index] = max_section_health
        elif commands[0] == "Status":
            for sections in pirate_ship_status:
                if sections < max_section_health * 0.2 :
                    repair_sections_count += 1
            print(f"{repair_sections_count} sections need repair.")
            repair_sections_count = 0

    else:
        break
print(f"Pirate ship status: {sum(pirate_ship_status)}\n\
Warship status: {sum(warship_ship_status)}")
