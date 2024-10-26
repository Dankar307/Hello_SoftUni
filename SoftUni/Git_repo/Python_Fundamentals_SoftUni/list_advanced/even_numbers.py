def isEven(even_nums):

    even_num_list = map(
        lambda x: x if even_nums[x] % 2 == 0 else "no",
        range(len(even_nums))
    )
    filtered_list = lambda a: list(filter(lambda a: a != "no", even_num_list))


    return even_num_list

even = list(map(int,input().split(", ")))
print(isEven(even))