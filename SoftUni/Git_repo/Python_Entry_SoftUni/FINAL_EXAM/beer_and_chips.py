from math import ceil
# Цената на една бира е 1.20 лв
# цената на един пакет чипс е равна на 45% от общата стойност на закупените бири
name = input()
starting_money = float(input())
num_of_beers = int(input())
num_of_chips = int(input())

beer_cost = num_of_beers * 1.2
chips_cost = ceil(num_of_chips * (beer_cost * 0.45))
whole_cost = chips_cost + beer_cost
if whole_cost <= starting_money:
    money_left = starting_money - whole_cost
    print(f"{name} bought a snack and has {money_left:.2f} leva left.")
else:
    money_needed = abs(starting_money - whole_cost)
    print(f"{name} needs {money_needed:.2f} more leva!")
