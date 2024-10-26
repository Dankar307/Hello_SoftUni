username = input()
av = []
commands = input()
while "Registration" not in commands:
    if "Letters" in commands:
        command, low_up = commands.split()
        if low_up == "Lower":
            username = username.lower()
            print(username)

        else:
            username = username.upper()
            print(username)
    elif "Reverse" in commands:
        command, start_index, end_index = commands.split()
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index in range(len(username)) and end_index in range(len(username)):

            for i in range(end_index, start_index- 1, -1):
                av.append(username[i])
            print("".join(av))
        else:

            continue
    elif "Substring" in commands:
        command, substring = commands.split()
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif "Replace" in commands:
        replace, char = commands.split()
        username = username.replace(char,"-")
        print(username)

    elif "IsValid" in commands:
        isvalid, char = commands.split()
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")

    commands = input()
