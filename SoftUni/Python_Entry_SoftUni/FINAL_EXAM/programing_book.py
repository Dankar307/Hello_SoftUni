price_per_page = float(input())
price_for_one_side = float(input())
percentage_of_discount = int(input())
designer_price = float(input())
percent_of_team_paycheck = float(input())

beggining_price = 899 * price_per_page + price_for_one_side * 2
discounted_price = beggining_price - beggining_price * (percentage_of_discount / 100)
whole_price = discounted_price + designer_price
final_price = whole_price - whole_price * (percent_of_team_paycheck / 100)

print(f"Avtonom should pay {final_price:.2f} BGN.")

