

numbers = input()
list_of_float_nums = numbers.split()
new_list = list(map(float,list_of_float_nums))
for i in range(0,len(new_list)):
    new_list[i] = round(new_list[i])



print(new_list)
