from collections import deque
queue = deque()
initial_water = int(input())

while True:

    name = input()
    if name == "Start":
        break
    queue.append(name)

command = input()
while command !="End":
    if command.isdigit():

        if int(command) <= initial_water:
            initial_water -= int(command)
            current_name = queue.popleft()
            print(f"{current_name} got water" )
        else:
            current_name = queue.popleft()
            print(f"{current_name} must wait" )
    elif command.startswith("refill"):
        _,current_water = command.split()
        initial_water += int(current_water)

    command = input()
print(f"{initial_water} liters left")