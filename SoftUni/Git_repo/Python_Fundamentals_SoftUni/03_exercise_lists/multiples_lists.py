factor = int(input())
count = int(input())
multiples = []
for ints in range(1, count + 1):
    new_multiple = factor * ints
    multiples.append(new_multiple)
multiples.sort()
print(multiples)