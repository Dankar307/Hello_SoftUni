list_with_tasks = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    importance = int(tokens[0]) - 1
    task = tokens[1]

    list_with_tasks.insert(importance, task)
result = [element for element in list_with_tasks if element != 0]
print(result)
