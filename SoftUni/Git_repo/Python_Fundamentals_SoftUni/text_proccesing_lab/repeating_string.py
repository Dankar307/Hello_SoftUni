list_of_str = input().split(" ")

string = "".join(word * len(word) for word in list_of_str)
print(string)