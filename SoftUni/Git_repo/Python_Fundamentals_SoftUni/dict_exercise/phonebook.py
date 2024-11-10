phonebook = {}
while True:
    current_input = input()
    if len(current_input) != 1:
        key, value = current_input.split("-")
        if key not in phonebook.keys():

            phonebook[key] = value  # potential error !!!
        else:
            continue
    else:
        break
N = int(current_input)
for i in range(N):
    search = input()
    if search in phonebook.keys():
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")