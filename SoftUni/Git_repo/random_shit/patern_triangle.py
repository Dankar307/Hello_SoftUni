size = int(input('Enter an intager: '))
for i in range(1,size+1):
    print(f'*')
    for j in range(0, i):
        print(f'*',end=' ')
print(f'*',end=' ')
