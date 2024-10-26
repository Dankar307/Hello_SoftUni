version_int = list(map(int, input().split(".")))
for i in range(len(version_int), 1, -1):
    version_int[i] += 1
    if version_int[i] >9:
        version_int[i] = 0
        version_int[i - 1] += 1
    break

for i in version_int:
    print(version_int[i]+ "." , end = "")