interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
counter_of_iterations = 0
flag = False
for n1 in range(interval, end_of_interval + 1):
    for n2 in range(interval, end_of_interval + 1):
        counter_of_iterations += 1
        if n1 + n2 == magic_number:
            flag = True
            print(f"Combination N:{counter_of_iterations} ({n1} + {n2} = {magic_number})")
            break
    if flag:
        break
if n1 + n2 != magic_number:
    print(f"{counter_of_iterations} combinations - neither equals {magic_number}")


