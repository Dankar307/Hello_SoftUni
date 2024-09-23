number_of_characters = int(input())
sum_of_chars = 0
if number_of_characters > 0 and number_of_characters <=  20:
    for chars in range(1, number_of_characters + 1):
        current_char = input()
        sum_of_chars += ord(current_char)
else:
    exit()
print(f"The sum equals: {sum_of_chars}")