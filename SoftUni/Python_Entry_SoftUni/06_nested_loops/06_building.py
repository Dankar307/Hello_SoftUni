floors = int(input())
rooms = int(input())
for num_of_floors in range(floors, 0, -1):
    print('')
    for num_of_rooms in range(0, rooms):
        if num_of_floors == floors:
            print(f'L{num_of_floors}{num_of_rooms}', end = ' ')
        elif num_of_floors % 2 == 0:
            print(f'O{num_of_floors}{num_of_rooms}', end = ' ')
        else:
            print(f'A{num_of_floors}{num_of_rooms}', end = ' ')
