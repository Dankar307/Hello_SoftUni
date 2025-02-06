import re
line = input()
while line:


    if line:
        pattern = r"(w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+)"

        match = re.search(pattern, line)
        if match:

            print(match.group(1))
    line = input()