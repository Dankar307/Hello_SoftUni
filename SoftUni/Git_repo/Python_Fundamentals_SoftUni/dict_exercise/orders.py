order = {}
command = input()
quantity = 0
price = 0
while command != "buy":
    name, price, quantity = command.split()
    if name not in order.keys():
        order[name] = {"price": float(price),"quantity": int(quantity)}
    else:
        order[name]["quantity"] += int(quantity)
        order[name]["price"] = float(price)

    command = input()
for item in order.keys():
    prices = order[item]["quantity"] * order[item]["price"]
    print(f"{item} -> {prices:.02f}")