n = input()

for j in range(1, int(n[2]) + 1):
    for m in range(1, int(n[1]) + 1):
        for i in range(1, int(n[0] ) + 1):
            print(f'{j} * {m} * {i} = {i * j * m};')