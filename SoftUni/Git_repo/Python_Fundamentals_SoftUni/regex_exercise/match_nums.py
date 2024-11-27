import re


list_with_nums = []
while True:
    line = input()
    if not line:
        break

    pattern = r"\d+"
    matches = re.findall(pattern,line)
    for match in matches:
        list_with_nums.append(match)

for num in list_with_nums:
    print(num, end=" ")