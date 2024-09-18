num_of_people_in_group = int(input())
num_of_nights = int(input())
cards_per_bought = int(input())
tickets_per_bought = int(input())

night_price = 20
card_price = 1.60
ticket_price = 6
whole_price = night_price * num_of_nights + card_price * cards_per_bought + ticket_price * tickets_per_bought

final_whole_price = whole_price * num_of_people_in_group
final_price = final_whole_price + final_whole_price * 0.25
print(f'{final_price:.2f}')