name_of_the_movie = input()
type_of_the_ticket = input()
quantity_of_tickets = int(input())
price_for_ticket = 0

if name_of_the_movie == 'A Star Is Born':

    if type_of_the_ticket == 'normal':
        price_for_ticket = 7.5
    elif type_of_the_ticket == 'luxury':
        price_for_ticket = 10.5
    elif type_of_the_ticket == 'ultra luxury':
        price_for_ticket = 13.5

elif name_of_the_movie == 'Bohemian Rhapsody':

    if type_of_the_ticket == 'normal':
        price_for_ticket = 7.35
    elif type_of_the_ticket == 'luxury':
        price_for_ticket = 9.45
    elif type_of_the_ticket == 'ultra luxury':
        price_for_ticket = 12.75

elif name_of_the_movie == 'Green Book':

    if type_of_the_ticket == 'normal':
        price_for_ticket = 8.15
    elif type_of_the_ticket == 'luxury':
        price_for_ticket = 10.25
    elif type_of_the_ticket == 'ultra luxury':
        price_for_ticket = 13.25

elif name_of_the_movie == 'The Favourite':

    if type_of_the_ticket == 'normal':
        price_for_ticket = 8.75
    elif type_of_the_ticket == 'luxury':
        price_for_ticket = 11.55
    elif type_of_the_ticket == 'ultra luxury':
        price_for_ticket = 13.95

prihodi = price_for_ticket * quantity_of_tickets
print(f'{name_of_the_movie} -> {prihodi:.2f} lv.')
