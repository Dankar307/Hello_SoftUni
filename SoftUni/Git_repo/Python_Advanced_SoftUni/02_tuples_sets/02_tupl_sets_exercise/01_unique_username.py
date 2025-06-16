N = int(input())
names = set()
for _ in range(N):
    names.add(input())
print(*names, sep="\n")