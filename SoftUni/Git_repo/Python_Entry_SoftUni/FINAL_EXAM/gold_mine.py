num_of_mines = int(input())
sum_of_gold = 0
for mines in range(1, num_of_mines + 1):
    average_gold_rate = float(input())
    num_of_days = int(input())
    for days in range(1, num_of_days + 1):
        sum_of_gold += int(input())
    average_gold = sum_of_gold / num_of_days
    if average_gold_rate <= average_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
        sum_of_gold = 0
    else:
        gold_needed = abs(average_gold - average_gold_rate)
        print(f"You need {gold_needed:.2f} gold.")
        sum_of_gold = 0