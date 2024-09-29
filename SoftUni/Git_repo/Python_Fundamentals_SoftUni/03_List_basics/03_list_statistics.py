numbers_count = int(input())
positive_integers = []
negative_integers = []
sum_of_negative = 0
count_of_positive = 0
for i in range(numbers_count):
    new_int = int(input())
    if new_int > 0:
        positive_integers.append(new_int)
        count_of_positive += 1
    elif new_int < 0:
        negative_integers.append(new_int)
        sum_of_negative += new_int
print(positive_integers)
print(negative_integers)
print(f"Count of positives: {count_of_positive}\nSum of negatives: {sum_of_negative}")


