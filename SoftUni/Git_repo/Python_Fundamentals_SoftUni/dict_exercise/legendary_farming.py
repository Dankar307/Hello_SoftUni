items = {"shards":0,"fragments":0,"motes":0}

not_obt = True
while not_obt:
    item_list = input().split()
    for i in range(0, len(item_list), 2):
        key = item_list[i + 1].lower()
        if key not in items.keys():
            value = int(item_list[i])
            items[key] = value
        else:
            value = int(item_list[i])
            items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            not_obt = False
            break
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            not_obt = False
            break
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            not_obt = False
            break
for i in items.keys():
    print(f"{i}: {items[i]}")