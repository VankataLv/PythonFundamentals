number_cmds = int(input())
parking_db = {}
for i in range(number_cmds):
    data = input().split()
    if data[0] == "register":
        user = data[1]
        plate = data[2]
        if user not in parking_db.keys():
            parking_db[user] = plate
            print(f"{user} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_db[user]}")
    elif data[0] == "unregister":
        user = data[1]
        if user not in parking_db.keys():
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            parking_db.pop(user)
for key, value in parking_db.items():
    print(f"{key} => {value}")

# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy

# 4
# register Jony AA4132BB
# register Jony AA4132BB
# register Linda AA9999BB
# unregister Jony
