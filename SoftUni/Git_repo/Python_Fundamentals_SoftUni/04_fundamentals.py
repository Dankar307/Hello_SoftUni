def calculate(a: float,b: float):
    return a + b


num1 = int(input())
num2 = int(input())

print(calculate(num1,num2))

x = lambda n1,n2: n1 + n2
num1 = float(input())
num2 = float(input())
print(x(num1,num2))