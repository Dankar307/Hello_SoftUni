def multiply(*args):
    mult = 1
    for num in range(len(args)):
        mult = mult * args[num]
    return mult




print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))