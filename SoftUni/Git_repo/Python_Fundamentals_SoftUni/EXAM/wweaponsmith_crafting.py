list_of_weapon_particles = input().split("|")
while True:
    command = input()
    if "Done" not in command:
        if "Add" in command:
            add_command, particle, index = command.split()

            if int(index) in range(len(list_of_weapon_particles)):
                list_of_weapon_particles.insert(int(index), particle)
            else:
                continue
        elif "Remove" in command:
            remove_cmd, index = command.split()
            index = int(index)
            if index in range(len(list_of_weapon_particles)):
                list_of_weapon_particles.remove(list_of_weapon_particles[index])
        else:
            for indexes in range(0, len(list_of_weapon_particles)):
                if "Even" in command and indexes % 2 == 0:

                    print(list_of_weapon_particles[indexes], end=" ")
                elif "Odd" in command and indexes % 2 != 0:
                    print(list_of_weapon_particles[indexes], end=" ")
            print()
    else:
        joined_list = "".join(list_of_weapon_particles)
        print(f"You crafted {joined_list}!")
        break
        