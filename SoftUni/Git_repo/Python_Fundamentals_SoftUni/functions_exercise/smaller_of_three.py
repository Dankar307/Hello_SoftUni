def smaller_number(a, b, c):
    if a > b and c > b:
        return b
    elif a < b and a < c:
        return a
    else:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(smaller_number(num1,num2,num3))