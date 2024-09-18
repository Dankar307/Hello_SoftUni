num_clients = int(input())
sum_products = 0
product_count = 0
discount = 0
day_average = 0

for client_num in range(1, num_clients + 1):

    while True:
        product = input()

        if product == 'basket':
            product_count += 1
            sum_products += 1.5
        elif product == 'wreath':
            product_count += 1
            sum_products += 3.8
        elif product == 'chocolate bunny':
            sum_products += 7
            product_count += 1
        else:
            break

    if product_count % 2 == 0:
        discount = 0.2


    if discount > 0:

        print(f"You purchased {product_count} items for {sum_products - sum_products * discount:.2f} leva.")
        day_average += sum_products - sum_products * discount
    else:
        print(f"You purchased {product_count} items for {sum_products:.2f} leva.")
        day_average += sum_products
    sum_products = 0
    product_count = 0

average_bill = day_average / num_clients
print(f"Average bill per client is: {average_bill:.2f} leva.")