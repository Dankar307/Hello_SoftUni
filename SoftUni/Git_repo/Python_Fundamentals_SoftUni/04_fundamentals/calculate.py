def calculate(a,b,operator):
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        if b > 0:
            result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


operator_str = input()
a = int(input())
b = int(input())
result_of_action = calculate(a,b,operator_str)
print(result_of_action)