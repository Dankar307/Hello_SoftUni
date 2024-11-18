string_for_replacement = input()
new_string = ""
last_char = ""
for char in string_for_replacement:
    if char == last_char:
        continue

    last_char = char
    new_string += char
print(new_string)