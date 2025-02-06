import re
total_calories = 0
some_lst = []
some_string = input()
pattern = r"\#[A-Za-z ]+\#[0-9]{2}\/[0-9]{2}\/[0-9]{2}\#[0-9]+\#|\|[A-Za-z]+\|[0-9]{2}\/[0-9]{2}\/[0-9]{2}\|[0-9]+\|"
matches = re.findall(pattern,some_string)


for match in range(len(matches)):
    if matches[match][0] == "#":
        shits = matches[match].split("#")
    else:
        shits = matches[match].split("|")
    total_calories += int(shits[3])
    some_lst.append(shits)

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for shit in some_lst:
    print(f"Item: {shit[1]}, Best before: {shit[2]}, Nutrition: {shit[3]}")