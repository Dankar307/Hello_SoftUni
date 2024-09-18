divisor = int(input())
boundary = int(input())
N = 0

for i in range(boundary, 0 , -1):

    result = i % divisor
    if result == 0:
        print(i)
        break
