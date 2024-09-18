team = input()
souvenir = input()
num_of_souvenirs_bought = int(input())
price_per_souvenir = 0
if team == 'Argentina':
    if souvenir == 'flags':
        price_per_souvenir = 3.25
    elif souvenir == 'caps':
        price_per_souvenir = 7.20
    elif souvenir == 'posters':
        price_per_souvenir = 5.10
    elif souvenir == 'stickers':
        price_per_souvenir = 1.25
    else:
        print("Invalid stock!")
        exit()


elif team == 'Brazil':
    if souvenir == 'flags':
        price_per_souvenir = 4.20
    elif souvenir == 'caps':
        price_per_souvenir = 8.50
    elif souvenir == 'posters':
        price_per_souvenir = 5.35
    elif souvenir == 'stickers':
        price_per_souvenir = 1.20
    else:
        print("Invalid stock!")
        exit()
elif team == 'Croatia':
    if souvenir == 'flags':
        price_per_souvenir = 2.75
    elif souvenir == 'caps':
        price_per_souvenir = 6.90
    elif souvenir == 'posters':
        price_per_souvenir = 4.95
    elif souvenir == 'stickers':
        price_per_souvenir = 1.10
    else:
        print("Invalid stock!")
        exit()
elif team == 'Denmark':
    if souvenir == 'flags':
        price_per_souvenir = 3.10
    elif souvenir == 'caps':
        price_per_souvenir = 6.50
    elif souvenir == 'posters':
        price_per_souvenir = 4.80
    elif souvenir == 'stickers':
        price_per_souvenir = 0.90
    else:
        print("Invalid stock!")
        exit()
else:
    print("Invalid country!")
    exit()
final_price = price_per_souvenir * num_of_souvenirs_bought
print(f'Pepi bought {num_of_souvenirs_bought} {souvenir} of {team} for {final_price:.2f} lv.')