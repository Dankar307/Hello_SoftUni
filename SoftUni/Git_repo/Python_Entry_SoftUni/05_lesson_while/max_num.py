from sys import maxsize
max_num = maxsize
while True:
    current_num = input()
    if current_num != 'Stop':
        current_num = int(current_num)
        if current_num < max_num:
            max_num = current_num

    else:
        print(f'{max_num}')
        break
