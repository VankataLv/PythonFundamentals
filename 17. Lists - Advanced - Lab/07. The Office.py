employee_hapiness = list(map(int, input().split(" ")))
factor = int(input())

new_employee_hapiness = [employee * factor for employee in employee_hapiness]
avg_happy = sum(new_employee_hapiness) / len(new_employee_hapiness)
happy_employees = [employee for employee in new_employee_hapiness if employee >= avg_happy]
sad_employees = [employee for employee in new_employee_hapiness if employee < avg_happy]
if len(happy_employees) >= len(new_employee_hapiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(new_employee_hapiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(new_employee_hapiness)}. Employees are not happy!")
