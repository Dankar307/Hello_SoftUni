string = input()
digit = ""
letters = ""
other = ""
for i in string:
    if i.isdigit():
        digit += i
    elif i.isalpha():
        letters += i
    else:
        other += i
print(digit)
print(letters)
print(other)