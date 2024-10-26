money_per_search = float(input())
number_of_users = int(input())
money_earned = 0
for user in range(1,number_of_users + 1):
    current_number_of_searches = int(input())

    if user % 3 == 0:

        if current_number_of_searches == 1:
            continue
        elif current_number_of_searches > 5:
            money_earned += (money_per_search * 6) * current_number_of_searches
            continue
        money_earned += (money_per_search * 3) * current_number_of_searches
    else:
        if current_number_of_searches > 5:

            money_earned += current_number_of_searches * money_per_search * 2
            continue
        elif current_number_of_searches == 1:
            continue
        money_earned += current_number_of_searches * money_per_search
print(f"Total money earned: {money_earned:.2f}")