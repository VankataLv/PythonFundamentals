pair_rows = int(input())
std_db = {}
for i in range(pair_rows):
    name = input()
    grade = float(input())
    if name not in std_db:
        std_db[name] = []
    std_db[name].append(grade)
for key in std_db:
    avg_grade = sum(std_db[key]) / len(std_db[key])
    if avg_grade >= 4.5:
        print(f"{key} -> {avg_grade:.2f}")
