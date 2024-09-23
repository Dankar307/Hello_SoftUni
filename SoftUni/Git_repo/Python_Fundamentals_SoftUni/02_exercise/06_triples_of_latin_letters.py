letter_num = int(input())
j = 0
k = 0
for i in range(0, letter_num):

    for j in range(0,letter_num):

        for k in range(0,letter_num):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97+k)}")