import re
matching = []
some_string = input()
pattern = r"#[A-za-z]{3,}##[A-za-z]{3,}#|@[A-za-z]{3,}@@[A-za-z]{3,}@"
matches = re.findall(pattern,some_string)
for match in matches:
    middle = len(match)//2
    first_match = match[:middle]
    second_match = match[middle:]
    clean_first = first_match.strip("@#")
    clean_second = second_match.strip("@#")
    if clean_first == clean_second[::-1]:
        matching.append(clean_first)

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if not matching:
    print("No mirror words!")

else:
    print("The mirror words are:")
    for match in range(len(matching)):
        reverse = matching[match][::-1]
        if match == len(matching)- 1:

            print(f"{matching[match]} <=> {reverse}")
        else:
            print(f"{matching[match]} <=> {reverse}", end=", ")