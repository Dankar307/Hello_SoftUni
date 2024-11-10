students = []
course_search = ''
while True:
    student_info = input()
    if ":" not in student_info:
        course_search = student_info
        break
    else:
        name, _id, course = student_info.split(":")
        students.append({"name": name, "id": _id, "course": course})

for student in students:
    if course_search.startswith(student["course"][0: 3]):
        print(f"{student["name"]} - {student["id"]}")
        continue