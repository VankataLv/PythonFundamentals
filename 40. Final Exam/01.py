txt = input()
cmd = input()
while cmd != "End":
    if cmd == "Lowercase":
        txt = txt.lower()
        print(txt)
    else:
        action, *info = cmd.split(" ")
        if action == "Translate":
            old_char = info[0]
            replacement = info[1]
            txt = txt.replace(old_char, replacement)
            print(txt)
        elif action == "Includes":
            sub_str = info[0]
            if sub_str in txt:
                print("True")
            else:
                print("False")
        elif action == "FindIndex":
            char = info[0]
            i_found = txt.rindex(char)
            print(i_found)
        elif action == "Remove":
            start_i = int(info[0])
            count = int(info[1])
            txt = txt[:start_i] + txt[start_i+count:]
            print(txt)
        elif action == "Start":
            sub_str = info[0]
            print(txt.startswith(sub_str))
    cmd = input()
