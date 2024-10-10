command = input()
price_without_tax = 0
tax_price = 0
if command == 'special' or command == 'regular':
    print("Invalid order!")
else:
    while command != 'special' and command != 'regular':
        part_cost = float(command)
        if part_cost > 0:
            price_without_tax += part_cost
            tax_price += part_cost * 0.2
            command = input()

        elif part_cost == 0:
            print("Invalid order!")
            command = input()
            continue
        elif part_cost < 0:
            print("Invalid price!")
            command = input()
            continue
    total_price = tax_price + price_without_tax
    if command == "special":
        total_price = total_price * 0.9
        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {price_without_tax:.2f}$\n"
              f"Taxes: {tax_price:.2f}$\n"
              f"-----------\n"
              f"Total price: {total_price:.2f}$\n")
    else:
        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {price_without_tax:.2f}$\n"
              f"Taxes: {tax_price:.2f}$\n"
              f"-----------\n"
              f"Total price: {total_price:.2f}$\n")