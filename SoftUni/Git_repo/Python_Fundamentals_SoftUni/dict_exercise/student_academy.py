number_of_students = int(input())
grades = {}
num_of_refer = {}
for student in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in grades.keys():
        grades[name] = grade
        num_of_refer[name] = 1
    else:
        grades[name] += grade
        num_of_refer[name] += 1

for name, grade in grades.items():
    average = grades[name] / num_of_refer[name]
    if average < 4.50:
        continue

    print(f"{name} -> {average:.2f}")