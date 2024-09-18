from math import ceil, floor
price_for_a_racket = float(input())
num_of_rackets = int(input())
num_of_shoes = int(input())
price_for_shoes = price_for_a_racket / 6

shoes = num_of_shoes * price_for_shoes
rackets = num_of_rackets * price_for_a_racket

other_equipment = (shoes + rackets) * 0.2
whole_price = other_equipment + rackets + shoes
price_for_djokovich = whole_price / 8
price_for_sponsors = whole_price - whole_price / 8
print(f"Price to be paid by Djokovic {floor(price_for_djokovich)}")
print(f'Price to be paid by sponsors {ceil(price_for_sponsors)}')