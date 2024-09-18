deposit_value = float(input())
# Стойност на депозита
deposit_period = int(input())
# Период на депозита
annual_interest_rate = float(input())
# Годишна стойност на лихвата
percent = annual_interest_rate/100

whole_of_year_interest = deposit_value * percent
month_interest = whole_of_year_interest / 12
final_sum = deposit_value + deposit_period * month_interest
print(final_sum)
