pocket_money = float(input())
money_earned_from_stand = float(input())
expences = float(input())
price_for_present = float(input())

saved_pocket_money = 5 * pocket_money
saved_money_earned_from_stand = 5 * money_earned_from_stand
saved_money_from_all = (saved_pocket_money + saved_money_earned_from_stand) - expences
if saved_money_from_all > price_for_present:
    print(f"Profit: {saved_money_from_all} BGN, the gift has been purchased.")
else:
    needed_money = abs(saved_money_from_all - price_for_present)
    print(f"Insufficient money: {needed_money:.2f} BGN.")
