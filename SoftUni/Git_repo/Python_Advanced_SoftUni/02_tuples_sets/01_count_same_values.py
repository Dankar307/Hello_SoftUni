sequence = [float(x) for x in input().split()]
set_of_nums = set(sequence)
for num in set_of_nums:
    occurences = sequence.count(num)
    print(f"{num} - {occurences} times")