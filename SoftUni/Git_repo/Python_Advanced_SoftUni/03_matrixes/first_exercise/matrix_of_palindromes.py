r,c = [int(x) for x in input().split()]


for row in range(r):
    start_letter = ord("a") + row
    for col in range(c):
        print(chr(start_letter)+chr(start_letter + col) + chr(start_letter), end=" ")
    print()