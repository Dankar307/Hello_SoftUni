initial_energy = int(input())
battles_won_counter = 1
while True:
    command = input()
    if command != "End of battle":
        command = int(command)

        if initial_energy - command <= 0:
            initial_energy -= command
            print(f"Not enough energy! Game ends with {battles_won_counter} won battles and {initial_energy} energy")

            exit()

        else:
            initial_energy -= command
            battles_won_counter += 1
        if battles_won_counter % 3 == 0:
            initial_energy += battles_won_counter

    else:
        print(f"Won battles: {battles_won_counter}. Energy left: {initial_energy}")
        break

