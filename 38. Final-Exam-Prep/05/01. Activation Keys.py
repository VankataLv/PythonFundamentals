act_key = input()
command = input()
while command != "Generate":
    action, tokens = command.split(">>>", 1)
    if action == "Contains":
        if tokens in act_key:
            print(f"{act_key} contains {tokens}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        tokens = tokens.split(">>>")
        start_i = int(tokens[1])
        end_i = int(tokens[2])
        if tokens[0] == "Upper":
            str_to_change = act_key[start_i:end_i]
            str_to_change = str_to_change.upper()
            act_key = act_key[:start_i] + str_to_change + act_key[end_i:]
        elif tokens[0] == "Lower":
            str_to_change = act_key[start_i:end_i]
            str_to_change = str_to_change.lower()
            act_key = act_key[:start_i] + str_to_change + act_key[end_i:]
        print(act_key)
    elif action =="Slice":
        tokens = tokens.split(">>>")
        start_i = int(tokens[0])
        end_i = int(tokens[1])
        str_to_del = act_key[start_i:end_i]
        act_key = act_key.replace(str_to_del, "")
        print(act_key)
    command = input()
print(f"Your activation key is: {act_key}")
