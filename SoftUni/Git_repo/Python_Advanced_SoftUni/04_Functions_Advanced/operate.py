def operate(operator, *args):
    result= 0
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = args[0]
        for item in range(1,len(args)):
            result -= args[item]
    elif operator == '*':
        result = args[0]
        for item in range(1,len(args)):
            result *= args[item]
    elif operator == '/':
        result = args[0]
        for item in range(1,len(args)):
            result /= args[item]
    return result
print(operate("*", 3, 4))