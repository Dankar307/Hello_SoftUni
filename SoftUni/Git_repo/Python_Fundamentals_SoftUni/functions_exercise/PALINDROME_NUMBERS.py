def is_palindrome(n):
    for i in n:
        if i == i[::-1]:
            return True
        else:
            return False
number = input().split(", ")
ints = []
for num in number:
    ints = int(num)
print(is_palindrome(ints))