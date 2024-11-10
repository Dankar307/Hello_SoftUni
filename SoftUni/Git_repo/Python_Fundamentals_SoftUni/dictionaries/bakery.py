bakery_list = input().split(" ")
bakery_dictionary = {}
for item in range(0, len(bakery_list), 2):
    key = bakery_list[item]
    value = bakery_list[item + 1]
    bakery_dictionary[key] = int(value)
print(bakery_dictionary)