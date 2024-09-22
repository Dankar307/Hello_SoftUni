task = input()
coffee_track = 0
while task != 'END':
    if task.lower() == "coding" or task.lower() == "cat" or task.lower() == "dog" or task.lower() == "movie":

        if task.isupper():
            coffee_track += 2
        else:
            coffee_track += 1
        task = input()
    else:
        task = input()
        continue
if coffee_track > 5:
    print('You need extra sleep')
else:
    print(coffee_track)