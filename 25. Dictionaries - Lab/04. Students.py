command = input()
students = {}
while ":" in command:
    name, stud_id, course = command.split(":")
    students[int(stud_id)] = {}
    students[int(stud_id)]['name'] = name
    students[int(stud_id)]['course'] = course
    command = input()

course_to_sort = " ".join(command.split("_"))
for key, value in students.items():
    if value["course"] == course_to_sort:
        print(f"{value['name']} - {key}")

# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals

# Alex:6:programming basics
# Maria:7:programming basics
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics