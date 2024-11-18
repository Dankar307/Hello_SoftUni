starting_string = input()
explosion_power = 0
final_string = ""
for index in range(len(starting_string)):

    if starting_string[index] != ">" and explosion_power > 0:
        explosion_power -= 1
    elif starting_string[index] == ">":
        final_string += starting_string[index]
        explosion_power += int(starting_string[index + 1])
    else:
        final_string += starting_string[index]
print(final_string)