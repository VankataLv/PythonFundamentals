from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
current_student_bonus = 0
highest_student_tendencies = 0

for student in range(students):
    count_attendances = int(input())
    current_student_bonus = count_attendances / lectures * (5 + additional_bonus)
    if current_student_bonus > max_bonus:
        max_bonus = current_student_bonus
        highest_student_tendencies = count_attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {highest_student_tendencies} lectures.")
