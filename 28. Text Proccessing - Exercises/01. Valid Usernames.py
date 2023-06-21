user_names = input().split(", ")

for user in user_names:
    if 3 <= len(user) <= 16:
        if user.isalnum() or "-" in user or "_" in user:
            if " " not in user:
                print(user)
