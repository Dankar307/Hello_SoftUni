string = input()
list_of_strings = string.split()
absolute_string = []
for i in list_of_strings:
    absolute_string.append(abs(float(i)))
print(absolute_string)