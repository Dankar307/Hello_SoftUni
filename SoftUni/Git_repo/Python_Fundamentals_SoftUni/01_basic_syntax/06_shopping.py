budget = int(input())
command = input()
price_of_product = 0
total_price = 0
while not command == 'End':

    price_of_product = int(command)
    budget -= price_of_product
    if budget < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print("You bought everything needed.")