def sort(number):
    list_int = []
    sorted_list = number
    for i in sorted_list:
        list_int.append(int(i))
    list_int = sorted(list_int)

    return list_int


num = input().split(" ")
print(sort(num))