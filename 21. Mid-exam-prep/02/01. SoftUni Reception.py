first_receptionist = int(input())
second_receptionist = int(input())
third_receptionist = int(input())
total_student_questions = int(input())
hours = 0
ans_hour = first_receptionist + second_receptionist + third_receptionist
while total_student_questions > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    else:
        total_student_questions -= ans_hour

print(f"Time needed: {hours}h.")
