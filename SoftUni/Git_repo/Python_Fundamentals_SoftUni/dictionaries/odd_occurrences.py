string_list = [string.lower() for string in input().split(" ")]
my_dictionaries = {}
occurrences = 0
for item in range(0, len(string_list)):
    key = string_list[item]
    if key in my_dictionaries.keys():
        my_dictionaries[key] += 1
    else:
        my_dictionaries[key] = 1
for item in my_dictionaries.keys():
    if my_dictionaries[item] % 2 != 0:
        print(item, end=" ")
