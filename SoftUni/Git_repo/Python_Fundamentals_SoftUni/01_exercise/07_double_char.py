command = input()

while command != 'End':
    if command != 'SoftUni':

        for character in command:
            print(character * 2, end='')
        print()
    command = input()