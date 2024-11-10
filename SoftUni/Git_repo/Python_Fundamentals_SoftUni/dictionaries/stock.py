stock_list = input().split(" ")
stock_dictionary = {}
for item in range(0, len(stock_list), 2):
    key = stock_list[item]
    value = stock_list[item + 1]
    stock_dictionary[key] = int(value)


searched_items = input().split(" ")
for item in searched_items:
    if item in stock_dictionary:
        print(f"We have {stock_dictionary[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")