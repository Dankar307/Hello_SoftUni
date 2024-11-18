string = input()
encrypted_str = ""
for char in string:
    encrypted_char =chr(ord(char) + 3)
    encrypted_str += encrypted_char
print(encrypted_str)