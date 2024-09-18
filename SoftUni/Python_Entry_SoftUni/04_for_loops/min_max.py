from sys import maxsize
n = int(input())
current_max = -maxsize
current_min = maxsize
for _ in range(n):
    current_number = int(input())

    if current_number > current_max:
        current_max = current_number

    if current_number < current_min:
        current_min = current_number

print(f"Max number: {current_max}")
print(f"Min number: {current_min}")
