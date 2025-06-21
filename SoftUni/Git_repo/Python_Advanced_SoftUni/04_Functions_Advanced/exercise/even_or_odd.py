def even_odd(*args):
    nums = args[:-1]
    command = args[-1]
    if command == "even":
        return [el for el in nums if el % 2 == 0]
    else:
        return [el for el in nums if el % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))