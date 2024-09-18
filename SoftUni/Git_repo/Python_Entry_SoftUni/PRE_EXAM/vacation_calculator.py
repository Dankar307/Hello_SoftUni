num_of_people_going = int(input())
season_of_the_year = input()
discount = 0
price_per_person = 0
if num_of_people_going <= 5:
    if season_of_the_year == "spring":
        price_per_person = 50.00
    elif season_of_the_year == "summer":
        price_per_person = 48.50 - 48.50 * 0.15
    elif season_of_the_year == "autumn":
        price_per_person = 60.00
    else:
        price_per_person = 86.00 + 86.00 * 0.08

else:

    if season_of_the_year == "spring":
        price_per_person = 48.00
    elif season_of_the_year == "summer":
        price_per_person = 45.0 - 45.0 * 0.15
    elif season_of_the_year == "autumn":
        price_per_person = 49.50
    else:
        price_per_person = 85.00 + 85.00 * 0.08

price_for_vacation = price_per_person * num_of_people_going
print(f'{price_for_vacation:.2f} leva.')
