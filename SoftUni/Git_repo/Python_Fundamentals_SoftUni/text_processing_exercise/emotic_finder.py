text = input().split()
last_index = 0
for strings in text:

    if ":" in strings:
        index = strings.index(":") + 1
        if index in range(len(strings)):
            print(f":{strings[index]}")
