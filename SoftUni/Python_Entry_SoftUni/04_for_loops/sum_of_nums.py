interator = int(input())
odd_sum = 0
even_sum = 0
difference = 0
for numbers in range(interator):
    if numbers % 2 == 0:
        even_sum = even_sum + int(input())
    else:
        odd_sum = odd_sum + int(input())

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {difference}")
