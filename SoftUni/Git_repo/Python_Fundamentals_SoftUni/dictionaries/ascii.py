list_of_chars = input().split(", ")
char_dict = {}
for char in list_of_chars:
    key = char
    value = int(ord(char))
    char_dict[key] = value
print(char_dict)