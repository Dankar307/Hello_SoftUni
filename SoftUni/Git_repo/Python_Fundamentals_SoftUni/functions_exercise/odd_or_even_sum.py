def sum_of_even(number):
    sum_of_even = 0
    for i in range(0, len(number)):
        if int(number[i]) % 2 == 0:
            sum_of_even += int(number[i])
    return sum_of_even


def sum_of_odd(number):
    sum_of_odd_n = 0
    for i in range(0, len(number)):
        if int(number[i]) % 2 != 0:
            sum_of_odd_n += int(number[i])
    return sum_of_odd_n
number = input()
print(f"Odd sum = {sum_of_odd(number)}, Even sum = {sum_of_even(number)}")