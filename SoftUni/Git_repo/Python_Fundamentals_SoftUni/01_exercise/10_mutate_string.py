first_string = input()
second_string = input()
last_printed_string = first_string
for characters in range(len(first_string)):

    left_half = second_string[:characters + 1]
    right_half = first_string[characters + 1:]
    full_string = left_half + right_half
    new_string = full_string
    if new_string == last_printed_string:
        continue
    else:
        print(new_string)
        last_printed_string = new_string
