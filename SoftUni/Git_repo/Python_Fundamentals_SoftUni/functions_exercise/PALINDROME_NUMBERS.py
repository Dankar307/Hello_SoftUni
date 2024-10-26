def is_palindrome(n):
    for i in n:
        return str(n) == ''.join(reversed(str(n)))


# Get the number from the user
n = input().split()

# Check if the number is a palindrome
if is_palindrome(n):
    print("True")
else:
    print("False")