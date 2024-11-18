banned_words_list = input().split(", ")
text = input()
for word in banned_words_list:
    while True:
        if word in text:
            filter_ = "*" * len(word)
            text = text.replace(word, filter_)
        else:
            break
print(text)