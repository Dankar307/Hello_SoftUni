# 2.00 – 2.99 - "Fail"
# 3.00 – 3.49 - "Poor"
# 3.50 – 4.49 - "Good"
# 4.50 – 5.49 - "Very Good"
# 5.50 – 6.00 - "Excellent"
student_grade_as_text = 0.0

def grade(grade : float):

    global student_grade_as_text

    if 2.00 <= grade <= 2.99:
        student_grade_as_text = "Fail"
    elif 3.00 <= grade <= 3.49:
        student_grade_as_text = 'Poor'
    elif 3.50 <= grade <= 4.49:
        student_grade_as_text = 'Good'
    elif 4.50 <= grade <= 5.49:
        student_grade_as_text = 'Very Good'
    elif 5.50 <= grade <= 6.00:
        student_grade_as_text = 'Excellent'

    return student_grade_as_text


student_grade = float(input())
print(grade(student_grade))