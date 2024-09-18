STACK_OF_PENS = 5.80
STACK_OF_MARKERS = 7.20
CLEANING_SPRAY = 1.20

num_of_pens = int(input())
num_of_markers = int(input())
liters_of_cleaning_fluid = int(input())
percentage_of_discount = int(input())

price_of_pens = num_of_pens * STACK_OF_PENS
price_of_markers = num_of_markers * STACK_OF_MARKERS
price_of_cleaning_fluid = liters_of_cleaning_fluid * CLEANING_SPRAY
whole_price = price_of_markers + price_of_pens + price_of_cleaning_fluid
final_price = whole_price - (whole_price * (percentage_of_discount/100))

print(final_price)
