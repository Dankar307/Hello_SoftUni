number_of_rooms = int(input())
free_chairs = 0
for room in range(1,number_of_rooms + 1):
    chairs, people = input().split(" ")
    if len(chairs) >= int(people):
        free_chairs = len(chairs) - int(people)
        continue

    else:
        print(f"{int(people) - len(chairs)} more chairs needed in room {room}")


