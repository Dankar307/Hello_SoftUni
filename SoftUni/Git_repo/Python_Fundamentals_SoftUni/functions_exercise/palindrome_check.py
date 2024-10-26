def is_palindrome(n):
    for i in n:
        if i == i[::-1]:
            print("True")
        else:
            print("False")
n = input().split(", ")
is_palindrome(n)