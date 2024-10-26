word_list = input().split()
filtered_list = [word for word in word_list if len(word) % 2 == 0]
for i in filtered_list:
    print(i)