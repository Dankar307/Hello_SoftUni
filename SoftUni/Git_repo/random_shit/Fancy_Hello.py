import time
def alphabet(word: str):
    word_storage = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    for char in word:
        for i in alphabet:
            print(f"{word_storage}{i}")
            time.sleep(0.02)
        word_storage += char
    print(word)
word = input()
alphabet(word)