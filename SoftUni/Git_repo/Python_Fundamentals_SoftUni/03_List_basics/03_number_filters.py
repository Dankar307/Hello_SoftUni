num_of_ints = int(input())
filtered_list = []
unfiltered_list = []
for i in range(num_of_ints):
    new_int = int(input())
    unfiltered_list.append(new_int)
command = input()
if command == 'even':
    for each_int in range(len(unfiltered_list)):
        if unfiltered_list[each_int] % 2 == 0:
            filtered_list.append(unfiltered_list[each_int])


elif command == 'odd':
    for each_int in range(len(unfiltered_list)):
        if unfiltered_list[each_int] % 2 != 0:
            filtered_list.append(unfiltered_list[each_int])

elif command == 'negative':
    for each_int in range(len(unfiltered_list)):
        if unfiltered_list[each_int] < 0:
            filtered_list.append(unfiltered_list[each_int])

else:
    for each_int in range(len(unfiltered_list)):
        if unfiltered_list[each_int] >= 0:
            filtered_list.append(unfiltered_list[each_int])
print(filtered_list)

