import re
names = input()

pattern = r"([0-9]{2})([-.\/])([A-Z][a-z]{2})\2([0-9]{4})"
result = re.findall(pattern, names)
for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")