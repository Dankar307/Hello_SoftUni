command = input()
my_dict = {}
while command != "stop":
    key = command
    if key not in my_dict.keys():
        my_dict[key] = int(input())
    else:
        my_dict[key] += int(input())

    command = input()
for resource, quantity in my_dict.items():
    print(f"{resource} -> {quantity}")