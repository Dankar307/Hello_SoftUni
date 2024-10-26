import math
from math import ceil
num_of_students = int(input())
lecture_number = int(input())
additional_bonus = int(input())
student_attendance = 0
max_bonus = 0
max_attendance = 0
for student in range(1,num_of_students):
    student_attendance= int(input())
    if student_attendance > lecture_number:
        continue
    current_student_bonus = student_attendance / lecture_number * (5 + additional_bonus)
    rounded_bonus = math.ceil(current_student_bonus)
    if rounded_bonus >= max_bonus or max_attendance <=  student_attendance:
        max_bonus = rounded_bonus
        max_attendance = student_attendance
print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {math.ceil(max_attendance)} lectures.")