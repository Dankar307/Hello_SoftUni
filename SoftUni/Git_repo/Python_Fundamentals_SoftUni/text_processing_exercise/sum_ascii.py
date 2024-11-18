first_str, second_str = input().split()
sum_of_str = 0
if len(first_str) > len(second_str):
    for char in range(len(second_str)):
        sum_of_str += ord(first_str[char]) * ord(second_str[char])
    for i in range(1, len(first_str) - len(second_str) + 1):
        sum_of_str += ord(first_str[-i])
elif len(first_str) < len(second_str):
    for char in range(len(first_str)):
        sum_of_str += ord(first_str[char]) * ord(second_str[char])
    for i in range(1,len(second_str) - len(first_str) +1):

        sum_of_str += ord(second_str[-i])
else:
    for char in range(len(first_str)):
        sum_of_str += ord(first_str[char]) * ord(second_str[char])
print(sum_of_str)