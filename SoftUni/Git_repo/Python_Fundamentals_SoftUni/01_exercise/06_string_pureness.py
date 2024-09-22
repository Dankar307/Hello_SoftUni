number_of_strings = int(input())
for strings in range(0, number_of_strings):

    new_string = input()
    if '.' in new_string or ',' in new_string or '_' in new_string:
        print(f"{new_string} is not pure!")
    else:
        print(f"{new_string} is pure.")