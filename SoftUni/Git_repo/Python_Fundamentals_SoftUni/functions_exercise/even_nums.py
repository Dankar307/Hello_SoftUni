list_str = input().split()
list_int = [int(number) for number in list_str]




def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


filtered_list = filter(is_even,list_int)
print(list(filtered_list))