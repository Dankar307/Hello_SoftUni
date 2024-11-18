companies = {}
while True:
    command = input()

    if command == "End":
        break

    company_name, id_ = command.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []
        companies[company_name].append(id_)
    if id_ in companies[company_name]:
        continue
    else:
        companies[company_name].append(id_)
for company in companies:
    print(company)
    for id_s in companies[company]:
        print(f"-- {id_s}")