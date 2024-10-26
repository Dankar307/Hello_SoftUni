num_of_wagons = int(input())
wagon_list = []
for i in range(num_of_wagons):
    wagon_list.append(0)
command = input()
while command != "End":
    if "add" in command:
        commands, people = command.split()
        people = int(people)
        wagon_list[-1] += people
    elif "insert" in command:
        insert, index, people = command.split()
        people = int(people)
        index = int(index)
        wagon_list[index] += people
    elif "leave" in command:
        leave, index, people = command.split()
        people = int(people)
        index = int(index)
        wagon_list[index] -= people
    command = input()
print(wagon_list)