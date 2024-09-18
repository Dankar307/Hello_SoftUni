budget = float(input())
statists = int(input())
price_for_statists = float(input())
money_left = 0
decor = budget * 0.1
if statists > 150:
    price_for_statists = price_for_statists - (price_for_statists * 0.1)
else:
    pass
whole_price = price_for_statists * statists + decor
if budget >= whole_price:
    money_left = budget - whole_price
    print(f"Action! \nWingard starts filming with {money_left:.2f} leva left.")
else:
    money_left = whole_price - budget
    print(f"Not enough money! \nWingard needs {money_left:.2f} leva more.")