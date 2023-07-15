internal_db = {}
test_scores = {}
cmd = input()
highest_score = 0
cur_score = 0
best_candidate = ""
while cmd != "end of contests":
    course, password = cmd.split(":")
    internal_db[course] = password
    cmd = input()
cmd = input()
while cmd != "end of submissions":
    contest, typed_password, username, points = cmd.split("=>")
    if contest in internal_db.keys():
        if typed_password == internal_db[contest]:
            points = int(points)
            if username in test_scores.keys():
                if contest in test_scores[username].keys():
                    if test_scores[username][contest] < points:
                        test_scores[username][contest] = points
                else:
                    test_scores[username][contest] = points
            else:
                test_scores[username] = {contest: points}
    cmd = input()
for candidate in test_scores:
    for course in test_scores[candidate]:
        cur_score += test_scores[candidate][course]
    if cur_score > highest_score:
        highest_score = cur_score
        best_candidate = candidate
    cur_score = 0
print(f"Best candidate is {best_candidate} with total {highest_score} points.")
print("Ranking:")
sorted_keys_lst = [key for key in test_scores.keys()]
sorted_keys_lst.sort()
sorted_values_lst = []
new_dict = {}
for student in sorted_keys_lst:
    print(student)
    for key_course, value_course in test_scores[student].items():
        sorted_values_lst.append(value_course)
        new_dict[value_course] = key_course
    sorted_values_lst.sort(reverse=True)
    for value in sorted_values_lst:
        print(f"#  {new_dict[value]} -> {value}")
    sorted_values_lst.clear()
