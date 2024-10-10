money_as_string = input().split(', ')
number_of_beggars_as_int = []
for money in money_as_string:
    number_of_beggars_as_int.append(int(money))
amount_of_beggars = int(input())
starting_index = 0
sum_of_beggars = []
sum_of_current_beggar =0
for beggars in range(0,amount_of_beggars):
    for beggar in range(starting_index, len(money_as_string), amount_of_beggars):
        sum_of_current_beggar += number_of_beggars_as_int[beggar]
    starting_index += 1
    sum_of_beggars.append(sum_of_current_beggar)
    sum_of_current_beggar = 0

print(sum_of_beggars)