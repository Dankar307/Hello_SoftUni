type_of_drink = input()
city = input()
quantity = float(input())
price = 0


if city == "Sofia":

    if type_of_drink == "coffee":
        price = 0.5
    elif type_of_drink == 'water':
        price = 0.8
    elif type_of_drink == 'beer':
        price = 1.20
    elif type_of_drink == 'sweets':
        price = 1.45
    else:
        price = 1.6

elif city == "Plovdiv":

    if type_of_drink == "coffee":
        price = 0.4
    elif type_of_drink == 'water':
        price = 0.7
    elif type_of_drink == 'beer':
        price = 1.15
    elif type_of_drink == 'sweets':
        price = 1.30
    else:
        price = 1.50

else:

    if type_of_drink == "coffee":
        price = 0.45
    elif type_of_drink == 'water':
        price = 0.70
    elif type_of_drink == 'beer':
        price = 1.10
    elif type_of_drink == 'sweets':
        price = 1.35
    else:
        price = 1.55


final_price = price * quantity
print(f"{final_price:.2f}")

