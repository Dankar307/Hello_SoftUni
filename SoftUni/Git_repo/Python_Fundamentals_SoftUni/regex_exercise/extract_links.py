import re

matches = []
while True:

    some_string  = input()
    if some_string:
        pattern = r"(w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+)"

        match = re.findall(pattern, some_string)
        matches.append(match)
        print(match)
    else:
        break
for match in matches:
    print(matches[0])