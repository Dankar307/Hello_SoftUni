N = int(input())
total = 0
price_for_coffee = 0
for i in range(N):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule >100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price_for_coffee = capsules_per_day * days * price_per_capsule
    print(f"The price for the coffee is: ${price_for_coffee:.2f}")
    total += price_for_coffee
    price_for_coffee = 0
print(f"Total: ${total:.2f}")



