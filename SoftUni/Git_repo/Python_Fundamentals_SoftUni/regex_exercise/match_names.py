import re
names = input()

pattern = r"(?i)\b_([a-z]+)\b"
matches = re.findall(pattern, names)
for name in range(len(matches)):
    if name + 1 in range(len(matches)):

        print(matches[name], end=",")
    else:
        print(matches[name])