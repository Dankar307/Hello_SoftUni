courses_students = {}
courses_numbers = {}
command = input()
while command != "end":
    course_name, student_name = command.split(" : ")
    key = course_name
    if key not in courses_students.keys() or student_name not in courses_students.values():
        courses_students[key] = student_name
        courses_numbers[key] = 1
    elif key in courses_students.keys():
        courses_students[key] = student_name
        courses_numbers[key] += 1
    command = input()
for courses in courses_students.keys():

    print(f"{courses}: {courses_numbers[courses]}")
    for students in courses_numbers:
        print(f"-- {courses_students[students]}")