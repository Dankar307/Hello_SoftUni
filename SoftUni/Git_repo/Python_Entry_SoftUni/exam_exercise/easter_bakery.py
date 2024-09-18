num_of_kozunaks = int(input())
sum_of_grade = 0
max_grade = 0
best_baker = ''
for _ in range(1, num_of_kozunaks + 1):
    name_of_baker = input()
    while True:
        grade = input()
        if grade == 'Stop':
            print(f"{name_of_baker} has {sum_of_grade} points.")
            if sum_of_grade > max_grade:
                max_grade = sum_of_grade
                best_baker = name_of_baker
                print(f"{best_baker} is the new number 1!")
            sum_of_grade = 0
            break
        else:
            sum_of_grade += int(grade)

print(f"{best_baker} won competition with {max_grade} points!")
