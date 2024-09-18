puzzle = 2.60
talking_doll = 3.00
teddy_bear = 4.10
minion = 8.20
toy_truck = 2.00
discount = 0


price_for_vacation = float(input())

num_puzzles = int(input())
num_talking_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_toy_trucks = int(input())

num_of_toys_sold = num_toy_trucks + num_minions + num_puzzles + num_teddy_bears + num_talking_dolls

if num_of_toys_sold >= 50:
    discount = 0.25
else:
    discount = 0

money_earned = puzzle * num_puzzles + talking_doll * num_talking_dolls + teddy_bear * num_teddy_bears + num_minions * minion + toy_truck * num_toy_trucks
discounted_price = money_earned - (money_earned * discount)
taxed_money = discounted_price - (discounted_price * 0.1)

if taxed_money >= price_for_vacation:
    money_left = taxed_money - price_for_vacation
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = price_for_vacation - taxed_money
    print(f"Not enough money! {money_left:.2f} lv needed.")




