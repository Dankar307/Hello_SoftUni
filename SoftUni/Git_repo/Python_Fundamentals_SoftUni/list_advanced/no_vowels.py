word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
word_without_vowels = [letter for letter in word if not letter.lower() in vowels]
print("".join(word_without_vowels))