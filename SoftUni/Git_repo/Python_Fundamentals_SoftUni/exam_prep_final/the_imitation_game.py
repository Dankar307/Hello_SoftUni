encrypted_message = input()
while True:
    command = input()
    if command == "Decode":
        break

    commands = command.split("|")
    if commands[0] == "Move":
        encrypted_message = encrypted_message[int(commands[1]):] + encrypted_message[:int(commands[1])]
    elif commands[0] == "Insert":
        encrypted_message = encrypted_message[:int(commands[1])] + commands[2] + encrypted_message[int(commands[1]):]
    elif commands[0] == "ChangeAll":

        encrypted_message = encrypted_message.replace(commands[1], commands[2])
print(f"The decrypted message is: {encrypted_message}")
