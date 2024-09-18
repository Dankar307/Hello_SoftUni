
minimal_budget = 0.00
sum_of_money = 0
while True:
    country_name = input()

    if country_name == 'End':
        break
    else:
        minimal_budget = float(input())
        while sum_of_money < minimal_budget:
            sum_of_money += float(input())

        else:
          print(f'Going to {country_name}!')
          sum_of_money = 0




