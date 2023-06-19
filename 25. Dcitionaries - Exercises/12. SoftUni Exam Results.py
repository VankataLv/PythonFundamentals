data = input()
std_sub = {}
lang = {}
to_ban = False
while data != "exam finished":
    if "banned" in data:
        user, action = data.split("-")
        for k in std_sub.keys():
            if user in k:
                to_ban = True
        if to_ban:
            std_sub.pop(k)
        to_ban = False
    else:
        std, language, points = data.split("-")
        points = int(points)
        if std in std_sub.keys():
            lang[language] += 1
            if points > std_sub[std][1]:
                std_sub[std][1] = points

        else:
            std_sub[std] = [language, points]
            if language in lang:
                lang[language] += 1
            else:
                lang[language] = 1
    data = input()

print("Results:")
for k, v in std_sub.items():
    print(f"{k} | {v[1]}")
print("Submissions:")
for k, v in lang.items():
    print(f"{k} - {v}")
