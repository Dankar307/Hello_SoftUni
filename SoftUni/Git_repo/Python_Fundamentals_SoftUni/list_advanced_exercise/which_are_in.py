looking_words = input().split(", ")
full_list = input().split(", ")
final_list = []
for i in looking_words:
    for j in full_list:
        if i in j:
            final_list.append(i)

            break
print(final_list)