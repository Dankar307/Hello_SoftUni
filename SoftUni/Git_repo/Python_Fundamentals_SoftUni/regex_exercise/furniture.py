import re

items = []
total_cost = 0
while True:
    command = input()
    if command == "Purchase":
        break

    pattern = r"(?i)>>\b([a-z]+)<<(\d+\.?\d*)!(\d+)\b"
    match =re.findall(pattern, command)
    if match:
        items.append(match[0][0])
        total_cost += float(match[0][1]) * float(match[0][2])
print("Bought furniture:")
for item in items:
    print(item)
print(f"Total money spend: {total_cost:.2f}")