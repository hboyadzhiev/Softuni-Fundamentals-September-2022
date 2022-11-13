employees = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    company_name = command[0]
    employee_id = command[1]
    if company_name not in employees.keys():
        employees[company_name] = []
    if employee_id not in employees[company_name]:
        employees[company_name].append(employee_id)

for key, value in employees.items():
    print(key)
    for id in value:
        print(f"-- {id}")


