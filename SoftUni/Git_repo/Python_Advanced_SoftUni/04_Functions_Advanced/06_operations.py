def operate(operator,*args):
    result = 0
    if operator == "+":

        for i in range(len(args)):
            result += args[i]
        return result
    elif operator == "-":
        result += args[0]
        for i in range(1,len(args)+1):
            result -= args[i]