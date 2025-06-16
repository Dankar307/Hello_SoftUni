N = int(input())
students_list = {}
for _ in range(N):
    name, grade = input().split()
    if name not in students_list:
        students_list[name] = [float(grade)]
    else:
        students_list[name].append(float(grade))
for student in students_list:
    sum_of_grades = 0

    for grades in students_list[student]:

        sum_of_grades += grades
    average = sum_of_grades / len(students_list[student])
    grade_ = " ".join(str(f"{x:.2f}") for x in students_list[student])
    print(f"{student} -> {grade_} (avg: {average:.2f})")