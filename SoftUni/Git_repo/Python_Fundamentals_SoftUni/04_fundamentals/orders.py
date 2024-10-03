def order(choice, quantity):
    if choice == 'coffee':
        return quantity * 1.5
    elif choice == 'water':
        return quantity * 1.0
    elif choice == 'coke':
        return quantity * 1.4
    else:
        return quantity * 2.0


order_choice = input()
quantity_of_products = int(input())

print(f'{order(order_choice, quantity_of_products):.2f}')