user_contests_scores = {}   # {key -> username : {key -> contest : points}}
order_inp_contests = []
individual_statistics_by_points = {}
cmd = input()                       # "{username} -> {contest} -> {points}"
while cmd != "no more time":
    username, contest, points = cmd.split(" -> ")
    points = int(points)
    if contest not in order_inp_contests:
        order_inp_contests.append(contest)
    if username in user_contests_scores:
        if contest in user_contests_scores[username]:
            if user_contests_scores[username][contest] < points:
                user_contests_scores[username] = {contest: points}
        else:
            user_contests_scores[username][contest] = points
    else:
        user_contests_scores[username] = {contest: points}
    cmd = input()

for contest in order_inp_contests:
    specific_contest = {}
    ordered_points = []
    ordered_names_by_points = {}
    for username in user_contests_scores:
        if contest in user_contests_scores[username]:
            specific_contest[username] = user_contests_scores[username][contest]
    for key, value in specific_contest.items():
        ordered_points.append(value)
        # if value not in ordered_names_by_points:
        #     ordered_names_by_points[value] = [key]
        # else:
        #     ordered_names_by_points[value].append(key)
    ordered_points.sort(reverse=True)

    print(f"{contest}: {len(specific_contest)} participants")
    row_num = 1
    for key, value in ordered_names_by_points.items():
        if len(ordered_names_by_points[key]) > 1:
            for name in ordered_names_by_points[key]:
                print(f"{row_num}. {name} <::> {key}")
                row_num += 1
        else:
            print(f"{row_num}. {value[0]} <::> {key}")
            row_num += 1
print("DB_____________________")
print(specific_contest)
print(ordered_points)
print(ordered_names_by_points)
