import re
place_list = input()
pattern = r"[\^\*]+([A-Za-z ]{6,})[\^\*]+[\D\W]+\+*([?\-\d.]+),([?\-\d.]+)\+*"
matches = re.findall(pattern,place_list)
for match in matches:
    if match:
        cordinates = match[1] + "," + match[2]
        print(f"Found {match[0]} at coordinates {cordinates}.")

if not matches:
    print("No valid artifacts found.")