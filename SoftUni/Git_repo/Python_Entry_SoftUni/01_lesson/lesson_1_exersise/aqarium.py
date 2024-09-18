length = int(input())
width = int(input())
height = int(input())
percent = float(input())

percent = percent/100
size = length * width * height
size = size * 0.001
water_percentage = (1 - percent) * size

print(water_percentage)

