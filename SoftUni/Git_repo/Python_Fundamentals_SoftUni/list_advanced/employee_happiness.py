list_of_employees_happiness = list(map(int,input().split()))
happiness_factor = int(input())
mapped_list = list(map(
    lambda x: x * happiness_factor, list_of_employees_happiness
))
avarage = sum(num for num in mapped_list) // len(list_of_employees_happiness)
happy_people = list(filter(
    lambda a: a >= avarage + 1, mapped_list
))

if len(happy_people) >= len(list_of_employees_happiness) // 2:


    print(f"Score: {len(happy_people)}/{len(list_of_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(list_of_employees_happiness)}. Employees are not happy!")