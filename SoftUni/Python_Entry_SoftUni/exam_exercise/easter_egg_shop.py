num_of_eggs_avelable = int(input())
sum_of_eggs_sold = 0
comand = input()
while comand != 'Close':





    if comand == 'Buy':
        num_of_eggs = int(input())
        if num_of_eggs > num_of_eggs_avelable:
            print("Not enough eggs in store!")
            print(f"You can buy only {num_of_eggs_avelable}.")
            break
        else:
            sum_of_eggs_sold += num_of_eggs
            num_of_eggs_avelable -= num_of_eggs

    else:
        num_of_eggs = int(input())
        num_of_eggs_avelable += num_of_eggs
    comand = input()
else:
    print(f'Store is closed!')
    print(f"{sum_of_eggs_sold} eggs sold.")

