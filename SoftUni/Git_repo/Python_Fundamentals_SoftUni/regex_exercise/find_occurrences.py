import re
sentence = input()
name = input()
pattern = fr"(?i)\b({name})\b"
matches = re.findall(pattern,sentence)
print(len(matches))