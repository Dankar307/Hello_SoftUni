some_strings = input().split()
total_sum = 0
for word in some_strings:
    if word[0].isupper():
        number = int(word[1:3])
        result = number / (ord(word[0]) - 64)

    else:
        number = int(word[1:3])
        result = number * ((ord(word[0]) - 94) - 2)

    if word[3].isupper():
        number = int(word[1:3])
        result -= ((ord(word[0]) - 94) - 14)

    elif word[3].islower():
        number = int(word[1:3])
        result += (ord(word[0]) - 64) + 1
    total_sum += result
print(f"{total_sum:.2f}")