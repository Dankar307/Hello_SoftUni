sqare_meters = float(input())

whole_price = sqare_meters * 7.61
discount = whole_price * 0.18

final_price = whole_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
