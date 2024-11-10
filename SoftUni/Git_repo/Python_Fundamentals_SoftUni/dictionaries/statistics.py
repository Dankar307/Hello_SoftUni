count_of_products = 0
sum_of_values = 0
stock_dictionary = {}
while True:
    command = input()
    if command != "statistics":

        stock_list = command.split(": ")

        for item in range(0, len(stock_list), 2):
            key = stock_list[item]
            value = stock_list[item + 1]

            sum_of_values += int(value)
            if key in stock_dictionary:
                stock_dictionary[key] += int(value)

            else:
                stock_dictionary[key] = int(value)
                count_of_products += 1
    else:
        print("Products in stock:")
        break
for item in stock_dictionary:
    print(f"- {item}: {stock_dictionary[item]}")
print(f"Total Products: {count_of_products}")
print(f"Total Quantity: {sum_of_values}")