string_with_numbers = input()
int_list = string_with_numbers.split(' ')
inverted_list = []

for i in range(len(int_list)):
    if i <= 0:
        inverted_list.append(f'-{int_list[i]}')
    elif i > 0:

        inverted_list.append(f'{int_list[i]}')


print(inverted_list)