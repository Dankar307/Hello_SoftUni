coffee_list = input().split()
number_of_commands = int(input())
for command_num in range(0, number_of_commands):
    command = input()
    if "Include" in command:
        commands = command.split()
        coffee_list.append(commands[1])
    elif "Remove" in command:
        commands = command.split()  # first or last [1] |||||   number of coffees needed to be removed [2]
        if not int(commands[2]) > len(coffee_list):

            if commands[1] == "first":
                for number_of_coffees in range(0, int(commands[2])):
                    coffee_list.remove(coffee_list[0])
            else:
                for number_of_coffees in range(0, int(commands[2])):
                    coffee_list.remove(coffee_list[-1])
        else:
            continue

    elif "Prefer" in command:
        commands = command.split()  # [1] = coffee index 1 , [2] = coffee index 2
        if int(commands[1]) in range(len(coffee_list)) and int(commands[2]) in range(len(coffee_list)):
            coffee_list[int(commands[1])], coffee_list[int(commands[2])] \
                = coffee_list[int(commands[2])], coffee_list[int(commands[1])]
        else:
            continue
    elif "Reverse" in command:
        coffee_list.reverse()
print(f"Coffees:")
print(" ".join(coffee_list))
