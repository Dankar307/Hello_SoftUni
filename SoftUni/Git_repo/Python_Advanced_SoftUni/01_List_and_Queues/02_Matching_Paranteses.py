expression = input()
stack = []
index = 0
for symbol in expression:

    if symbol == "(":
        stack.append(index)
    elif symbol == ")":
        print(expression[stack.pop():index+1])

    index += 1

