string = input()
string = string.replace(" ", "")
my_dict = {}
for i in range(len(string)):
    key = string[i]
    if key not in my_dict.keys():
        my_dict[key] = 1
    else:
        my_dict[key] += 1
for keys, quantities in my_dict.items():
    print(f"{keys} -> {quantities}")