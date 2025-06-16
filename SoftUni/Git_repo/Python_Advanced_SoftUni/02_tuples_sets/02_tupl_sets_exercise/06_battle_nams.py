N = int(input())
even_set = set()
odd_set = set()

for i in range(1,N+1):
    sum_of_name = 0
    name = input()
    for ch in name:
        sum_of_name += ord(ch)
    sum_of_name = int(sum_of_name/i)
    if sum_of_name % 2 == 0:
        even_set.add(sum_of_name)
    else:
        odd_set.add(sum_of_name)
sum_of_even_set =sum(even_set)
sum_of_odd_set = sum(odd_set)
if sum_of_even_set == sum_of_odd_set:
    print(*even_set.union(odd_set), sep=", ")
elif sum_of_odd_set > sum_of_even_set:
    print(*odd_set.difference(even_set),sep=", ")
else:
    print(*even_set.symmetric_difference(odd_set),sep=", ")
