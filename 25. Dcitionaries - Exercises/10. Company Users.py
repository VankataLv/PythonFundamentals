db = {}
command = input()
while command != "End":
    company, emp_id = command.split(" -> ")
    if company not in db.keys():
        db[company] = []
    if emp_id not in db[company]:
        db[company].append(emp_id)
    command = input()

for company, employee_sheet in db.items():
    print(company)
    for el in employee_sheet:
        print(f"-- {el}")
