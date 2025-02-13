
courses = {}

while True:
    line = input()

    if line.lower() == "end":
        break

    course_name, student_name = line.split(" : ")

    if course_name not in courses:
        courses[course_name] = {}

    courses[course_name][student_name] = True

for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")

