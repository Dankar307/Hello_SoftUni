from math import pi
type_of_figure = input()
area = 0

if type_of_figure == "square":
    a = float(input())
    area = a * a

elif type_of_figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b

elif type_of_figure == "circle":
    r = float(input())
    area = pi * (r ** 2)

elif type_of_figure == "triangle":
    b = float(input())
    h = float(input())
    area = 1/2 * b * h

print(f"{area:.3f}")
