galaxy = {}
command = input()
new_jedi = True
old_jedi = False
while command != "Lumpawaroo":
    if "|" in command:
        side, user = command.split(" | ")
        if side not in galaxy:
            galaxy[side] = []
            galaxy[side].append(user)
        else:
            for k, v in galaxy.items():
                if user in v:
                    new_jedi = False
                else:
                    continue
            if new_jedi:
                galaxy[side].append(user)
            new_jedi = False
    elif "->" in command:
        user, side = command.split(" -> ")
        if side not in galaxy.keys():
            galaxy[side] = []
            galaxy[side].append(user)
        else:
            for k, v in galaxy.items():
                if user in v:
                    continue
                else:
                    old_jedi = False
            if not old_jedi:
                for k, v in galaxy.items():
                    if user in v:
                        old_k = k
                        v.remove(user)
                    else:
                        new_k = k
                galaxy[new_k].append(user)
                print(f"{user} joins the {new_k} side!")
            old_jedi = False
    command = input()

for k,v in galaxy.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for el in v:
            print(f"! {el}")
