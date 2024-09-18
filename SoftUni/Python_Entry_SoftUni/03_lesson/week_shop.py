fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
if not (day_of_week == 'Saturday' or day_of_week == 'Sunday'):

    if fruit == 'banana':
        price = 2.5

    if fruit == 'apple':
        price = 1.2
    if fruit == 'orange':
        price = 0.85
    if fruit == 'grapefruit':
        price = 1.45
    if fruit == 'kiwi ':
        price = 2.70
    if fruit == 'pineapple':
        price = 5.50
    if fruit == 'grapes':
        price = 3.85
    else:
        print("error")

else:
    if fruit == 'banana':
        price = 2.70
    if fruit == 'apple':
        price = 1.25
    if fruit == 'orange':
        price = 0.90
    if fruit == 'grapefruit':
        price = 1.60
    if fruit == 'kiwi':
        price = 3.00
    if fruit == 'pineapple':
        price = 5.60
    if fruit == 'grapes':
        price = 4.20
    else:
        print("error")


final_price = price * quantity
print(f'{final_price:.2f}')
