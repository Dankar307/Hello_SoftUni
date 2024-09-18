student_name = input()
num_of_fails = 0
year_count = 0
average_grade = 0.00
while True:

    year_count += 1
    if year_count <= 12:
        annual_grade = float(input())
        if annual_grade > 4.00:

            average_grade += annual_grade

        else:

            num_of_fails += 1

            if num_of_fails == 2:
                print(f"{student_name} has been excluded at {year_count - 1} grade")
                break
            else:
                continue
    else:
        print(f'{student_name} graduated. Average grade: {average_grade / 12:.2f}')
        break
