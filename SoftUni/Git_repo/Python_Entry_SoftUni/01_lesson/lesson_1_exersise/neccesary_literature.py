from math import floor
number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

time_for_book = number_of_pages / pages_per_hour
average_time = time_for_book / number_of_days

print(floor(average_time))
