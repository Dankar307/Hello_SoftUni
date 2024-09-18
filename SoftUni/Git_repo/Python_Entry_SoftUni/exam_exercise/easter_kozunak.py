from math import ceil
num_of_kozunaks = int(input())
max_used_sugar = 0
max_used_flour = 0
sum_of_sugar = 0
sum_of_flour = 0
for _ in range(1, num_of_kozunaks + 1):
    sugar_needed = int(input())
    flour_needed = int(input())
    if max_used_flour < flour_needed:
        max_used_flour = flour_needed
    if max_used_sugar < sugar_needed:
        max_used_sugar = sugar_needed
    sum_of_flour += flour_needed
    sum_of_sugar += sugar_needed
sugar_packs = ceil(sum_of_sugar / 950)
flour_packs = ceil(sum_of_flour / 750)
print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.")
