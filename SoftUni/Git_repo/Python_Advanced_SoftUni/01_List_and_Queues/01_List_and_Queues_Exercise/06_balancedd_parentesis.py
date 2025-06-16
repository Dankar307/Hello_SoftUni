expression = input()
parenetsis = {"{":"}","(":")","[":"]"}
stack = []
for symbol in expression:

    if symbol in parenetsis:
        stack.append(symbol)
    else:
        if not stack:
            print("NO")
            exit()
        last_printed_symbol = stack.pop()
        par = parenetsis[last_printed_symbol]
        if par == symbol:
            continue
        else:
            print("NO")
            exit()

print("YES")