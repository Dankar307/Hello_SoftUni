people_count = int(input())
elevator_size = int(input())


course_count = int(people_count / elevator_size)
if people_count % elevator_size != 0:
    course_count += 1
print(course_count)