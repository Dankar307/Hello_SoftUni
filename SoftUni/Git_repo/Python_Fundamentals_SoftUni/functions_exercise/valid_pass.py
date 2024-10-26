num_of_ints = 0
nums = ["1", "2", "3", "4", "5", "6","7","8" ,"9" ,"0"]
def is_valid(password):
    num_of_ints = 0
    digits_num = True
    isalnum = True
    int_check = True
    if len(password) < 6 or len(password) >= 10:
        print("Password must be between 6 and 10 characters")
        digits_num = False
    if password.isalnum() == False:
        print("Password must consist only of letters and digits")
        isalnum = False
    for i in nums:
        if i in password:
            num_of_ints += 1
        else:
            continue
    if num_of_ints < 2:
        print("Password must have at least 2 digits")
        int_check = False
    if digits_num and isalnum and int_check:
        print("Password is valid")


password = input()
is_valid(password)