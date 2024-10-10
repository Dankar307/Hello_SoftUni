gifts_str = input().split()
command = input()
str_command = []
while command != "No Money":
    if "OutOfStock" in command:
        str_command = command.split()
        if str_command[1] in gifts_str:
            
            gifts_str.remove(str_command[1])
    elif "Required" in command:
        pass
    elif "JustInCase" in command:
        pass
    command = input()
