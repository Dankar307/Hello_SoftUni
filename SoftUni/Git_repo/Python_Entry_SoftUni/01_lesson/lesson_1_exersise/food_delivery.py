chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50

num_chicken_menus = int(input())
num_fish_menus = int(input())
num_vegetarian_menus = int(input())

price_chick_menus = num_chicken_menus * chicken_menu
price_fish_menus = num_fish_menus * fish_menu
price_vegetarian_menus = num_vegetarian_menus * vegetarian_menu
whole_price = price_fish_menus + price_vegetarian_menus + price_chick_menus
deserts = whole_price * 0.2
final_price = whole_price + deserts + delivery

print(f"{final_price}")



