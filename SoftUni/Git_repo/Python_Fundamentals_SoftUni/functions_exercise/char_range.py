def chars_range(str1,str2):
    starting_value = ord(str1)
    ending_value = ord(str2)
    for chars in range(starting_value + 1, ending_value):
        print(chr(chars), end= " ")

string1 = input()
string2 = input()
chars_range(string1,string2)





