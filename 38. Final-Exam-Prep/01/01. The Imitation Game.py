encrypted_msg = input()
command = input()
while command != "Decode":
    tokens = command.split("|")
    if tokens[0] == "Move":
        str_to_cut = encrypted_msg[:int(tokens[1])]
        rest_of_str = encrypted_msg[int(tokens[1]):]
        encrypted_msg = rest_of_str + str_to_cut
    elif tokens[0] == "Insert":
        ind = int(tokens[1])
        str_to_ins = (tokens[2])
        new_msg = encrypted_msg[:ind] + str_to_ins + encrypted_msg[ind:]
        encrypted_msg = new_msg
    elif tokens[0] == "ChangeAll":
        old_str = tokens[1]
        new_str = tokens[2]
        encrypted_msg = encrypted_msg.replace(old_str, new_str)
    command = input()
print(f"The decrypted message is: {encrypted_msg}")
