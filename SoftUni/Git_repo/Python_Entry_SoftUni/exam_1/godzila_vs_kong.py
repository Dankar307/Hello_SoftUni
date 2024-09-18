film_budget = float(input())
statists = int(input())
price_for_clothes = float(input())
money_left = 0
decor = film_budget * 0.1

if statists >= 150:
    price_for_clothes = price_for_clothes - (price_for_clothes * 0.1)

whole_price = price_for_clothes * statists + decor

if film_budget >= whole_price:
    money_left = abs(film_budget - whole_price)
    print(f'Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
else:
    money_left = abs(film_budget - whole_price)
    print(f'Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')
