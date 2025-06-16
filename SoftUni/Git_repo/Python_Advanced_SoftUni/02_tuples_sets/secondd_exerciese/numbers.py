first_set = set(int(i) for i in input().split())
second_set = set(int(i) for i in input().split())
N = int(input())


for commands in range(N):
    command = input().split()
    curr_comman = command[0] + " " + command[1]
    numbers = [int(x) for x in command[2:]]
    if curr_comman == "Add First":


        first_set.update(numbers)

    elif curr_comman == "Add Second":
        second_set.update(numbers)
    elif curr_comman == "Remove First":
        first_set.difference_update(numbers)
    elif curr_comman == "Remove Second":
        second_set.difference_update(numbers)
    elif curr_comman == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))
print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")