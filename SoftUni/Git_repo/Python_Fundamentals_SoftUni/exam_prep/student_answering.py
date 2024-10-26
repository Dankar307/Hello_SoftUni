import math
from math import ceil
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
student_count = int(input())

hours_needed = math.ceil(student_count / (first_employee + second_employee+ third_employee ))
hours_needed += math.ceil(hours_needed // 4)

print(f"Time needed: {hours_needed}h.")