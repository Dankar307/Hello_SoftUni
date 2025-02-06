import re
destination_text = input()
destination_points = 0
match_list = []
pattern = r"=\b[A-z][A-za-z]{3,}\b=|\/\b[A-z][A-za-z]{3,}\b\/"
matches = re.findall(pattern,destination_text)
for match in matches:
    clean_match = match.strip("=/")
    destination_points += len(clean_match)

    match_list.append(clean_match)
destinations = ", ".join(match_list)
print(f"Destinations: {destinations}")
print(f"Travel Points: {destination_points}")