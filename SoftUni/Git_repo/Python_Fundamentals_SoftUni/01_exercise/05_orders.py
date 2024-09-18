N = int(input())
total = 0
price_for_coffee = 0
for i in range(N):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    price_for_coffee = capsules_per_day * days * price_per_capsule
    if price_for_coffee > 0:
        print(f"The price for the coffee is: ${price_for_coffee:.2f}")
    total += price_for_coffee
    price_for_coffee = 0
print(f"Total: ${total:.2f}")



