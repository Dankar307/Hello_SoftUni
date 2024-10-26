train_ticket_price = 150
items_for_buying = input().split("|")
budget = int(input())
clothes_max_price = 50
shoe_max_price = 35
accessories_max_price = 20.5
money_for_shopping = 0
money_from_selling = 0
selling_price_list = []
profit = 0
for items in items_for_buying:
    current_item, current_price = items.split("->")
    current_price = float(current_price)
    if budget < current_price:
        continue
    else:

        if current_item == "Clothes" and current_price <= clothes_max_price:
            budget -= current_price
            selling_price = current_price * 1.4
            money_for_shopping += current_price
            money_from_selling += selling_price
            selling_price_list.append(f"{selling_price:.2f}")
        elif current_item == "Shoes" and current_price <= shoe_max_price:
            budget -= current_price
            selling_price = current_price * 1.4
            money_for_shopping += current_price
            money_from_selling += selling_price
            selling_price_list.append(f"{selling_price:.2f}")
        elif current_item == "Accessories" and current_price <= accessories_max_price:
            budget -= current_price
            selling_price = current_price * 1.4
            money_for_shopping += current_price
            money_from_selling += selling_price
            selling_price_list.append(f"{selling_price:.2f}")
print(" ".join(selling_price_list))
profit = money_from_selling - money_for_shopping
print(f"Profit: {profit:.2f}")
if budget + money_from_selling >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
