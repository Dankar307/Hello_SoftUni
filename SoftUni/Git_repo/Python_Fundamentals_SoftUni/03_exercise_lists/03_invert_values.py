string_with_numbers = input()
int_list = list(map(int, string_with_numbers.split(' ')))
inverted_list = []

for i in range(len(int_list)):
    inverted_list.append(-int_list[i])


print(inverted_list)