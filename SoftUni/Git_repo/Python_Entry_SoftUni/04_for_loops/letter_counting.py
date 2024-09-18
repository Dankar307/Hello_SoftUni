word = input()
points = 0
for letters in word:
    if letters == 'a':
        points = points + 1
    elif letters == 'e':
        points = points + 2
    elif letters == 'i':
        points = points + 3
    elif letters == 'o':
        points = points + 4
    elif letters == 'u':
        points = points + 5

else:
    print(points)
