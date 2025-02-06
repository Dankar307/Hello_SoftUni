message = input()

while True:
    command = input().strip()

    if command == "Finalize":
        break

    if command.startswith("Encrypt"):
        message = message[::-1]
        print(message)

    elif command.startswith("Decrypt"):
        message = message.swapcase()
        print(message)

    elif command.startswith("Substitute"):

        commands = command.split()
        old_char = commands[1]
        new_char = commands[2]
        if old_char in message:
            message = message.replace(old_char, new_char)
            print(message)
        else:
            print("Character not found.")


    elif command.startswith("Scramble"):
        commands = command.split()
        index = int(commands[1])
        char = commands[2]
        if index in range(len(message)):
            message = message[:index] + char + message[index + 1:]
            print(message)
        else:
            print("Index out of bounds.")


    elif command.startswith("Remove"):

        commands = command.split(maxsplit=1)
        substring = commands[1]

        message = message.replace(substring, "")
        print(message)



    else:
        print("Invalid command detected!")

