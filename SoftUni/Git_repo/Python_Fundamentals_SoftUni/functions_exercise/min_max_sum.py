list_str = input().split()
list_int = [int(num) for num in list_str]

list_min = min(list_int)
list_max = max(list_int)
list_sum = sum(list_int)
print(f"The minimum number is {list_min}")
print(f"The maximum number is {list_max}")
print(f"The sum number is: {list_sum}")