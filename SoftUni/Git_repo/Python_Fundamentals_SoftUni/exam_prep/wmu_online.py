initial_health = 100
initial_bitcoin = 0
healed_amount = 0
dungeon_rooms = input().split("|")
for room in range(0, len(dungeon_rooms)):
    command, number = dungeon_rooms[room].split(" ")
    number = int(number)
    if command == "potion":
        if initial_health + number > 100:
            healed_amount = 100 - initial_health
            initial_health = 100
            print(f"You healed for {healed_amount} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            healed_amount = number
            initial_health += number
            print(f"You healed for {healed_amount} hp.")
            print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        initial_bitcoin += number
    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}." )
            print(f"Best room: {room + 1}")
            break

else:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {initial_health}")