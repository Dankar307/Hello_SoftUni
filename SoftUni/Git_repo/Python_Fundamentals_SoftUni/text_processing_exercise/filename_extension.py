filepath = input().split("\\")

file_name,extension = filepath[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")