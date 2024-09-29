number_of_strings = int(input())
special_word = input()
unfiltered_list = []
filtered_list = []
for i in range(number_of_strings):
    strings = input()
    unfiltered_list.append(strings)
    if special_word in strings:
        filtered_list.append(strings)
print(unfiltered_list)
print(filtered_list)
