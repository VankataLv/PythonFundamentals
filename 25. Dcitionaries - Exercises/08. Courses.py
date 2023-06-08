db = {}
command = input()
while command != "end":
    course, std_name = command.split(" : ")
    if course in db.keys():
        db[course].append(std_name)
    else:
        db[course] = []
        db[course].append(std_name)
    command = input()

for key, value in db.items():
    print(f"{key}: {len(value)}")
    for el in value:
        print(f"-- {el}")

# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end

# Algorithms : Jay Moore
# Programming Basics : Martin Taylor
# Python Fundamentals : John Anderson
# Python Fundamentals : Andrew Robinson
# Algorithms : Bob Jackson
# Python Fundamentals : Clark Lewis
# end
