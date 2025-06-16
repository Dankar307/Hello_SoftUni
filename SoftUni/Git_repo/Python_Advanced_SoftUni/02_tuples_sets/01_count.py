sequence = [float(x) for x in input().split()]
my_dict = {}
for num in sequence:
    if num not in my_dict.keys():
        my_dict[num] = 1
    else:
        my_dict[num] += 1
for n in my_dict.keys():
    print(f"{n} - {my_dict[n]} times")