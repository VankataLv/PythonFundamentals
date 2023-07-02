concealed = input()
command = input()
while command != "Reveal":
    action, details = command.split(":|:", 1)
    if action == "InsertSpace":
        details = int(details)
        first_part = concealed[:details]
        second_part = concealed[details:]
        concealed = first_part + " " + second_part
        print(concealed)
    elif action == "Reverse":
        if details in concealed:
            rev_details = details[::-1]
            concealed = concealed.replace(details, "", 1)
            concealed += rev_details
            print(concealed)
        else:
            print("error")
    elif action == "ChangeAll":
        old_text, replacement = details.split(":|:")
        concealed = concealed.replace(old_text, replacement)
        print(concealed)
    command = input()
print(f"You have a new text message: {concealed}")
