from sys import *
number_of_snowballs = int(input())
if number_of_snowballs >= 0 and number_of_snowballs <= 100:

    max_value = -maxsize
    max_weight = 0
    max_time = 0
    max_quality = 0
    for snowballs in range(1, number_of_snowballs):
        weight_of_a_snowball = int(input())
        time_needed_per_snowball = int(input())
        quality_of_a_snowball = int(input())
        snowball_value = (weight_of_a_snowball / time_needed_per_snowball) ** quality_of_a_snowball
        if snowball_value > max_value:
            max_value = snowball_value
            max_time = time_needed_per_snowball
            max_quality = quality_of_a_snowball
            max_weight = weight_of_a_snowball

    print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")