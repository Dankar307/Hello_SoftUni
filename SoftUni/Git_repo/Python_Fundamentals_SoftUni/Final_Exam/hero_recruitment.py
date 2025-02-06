hero_collection = {}
while True:
    command = input().split()

    if command[0] == "End":
        break

    if command[0] == "Enroll":
        hero = command[1]
        if hero not in hero_collection.keys():
            hero_collection[hero] = {}
        else:
            print(f"{hero} is already enrolled.")
    elif command[0] == "Learn":
        hero, spell = command[1],command[2]
        if hero not in hero_collection.keys():
            print(f"{hero} doesn't exist.")

        elif spell not in hero_collection[f"{hero}"].values():
            hero_collection[f"{hero}"][f"{spell}"] = spell

        else:
            print(f"{hero} has already learnt {spell}.")

    elif command[0] == "Unlearn":
        hero, spell = command[1],command[2]
        if hero not in hero_collection.keys():
            print(f"{hero} doesn't exist.")
        elif spell not in hero_collection[hero].values():
            print(f"{hero} doesn't know {spell}.")
        else:
            hero_collection[f"{hero}"].pop(f"{spell}")
print("Heroes:")
for heroes in hero_collection:
    spells = ", ".join(hero_collection[heroes].values())
    print(f"== {heroes}: {spells}")