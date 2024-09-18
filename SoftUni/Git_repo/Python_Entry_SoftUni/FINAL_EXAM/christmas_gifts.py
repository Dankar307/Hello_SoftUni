# Цената на всяка играчка е 5 лв., а цената на един пуловер е 15 лв.
kids_count = 0
adults_count = 0
sum_of_money_for_kids = 0
sum_of_money_for_adults = 0
while True:
    age = input()
    if age == "Christmas":
        break
    else:
        age = int(age)
        if age <= 16:
            kids_count += 1
            sum_of_money_for_kids += 5
        else:
            adults_count += 1
            sum_of_money_for_adults += 15

print(f"Number of adults: {adults_count}")
print(f"Number of kids: {kids_count}")
print(f"Money for toys: {sum_of_money_for_kids}")
print(f"Money for sweaters: {sum_of_money_for_adults}")