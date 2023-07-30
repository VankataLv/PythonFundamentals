psrd = input()
command = input()
while command != "Done":
    if command == "TakeOdd":
        new_psrd = ""
        for ind in range(1, len(psrd), 2):
            new_psrd += psrd[ind]
        psrd = new_psrd
        print(psrd)
    else:
        action, first, second = command.split(" ")
        if action == "Cut":
            ind = int(first)
            length = int(second)
            sub_string_to_cut = ""
            for i in range(ind, ind+length):
                sub_string_to_cut += psrd[i]
            psrd = psrd.replace(sub_string_to_cut, "", 1)
            print(psrd)
        elif action == "Substitute":
            sub_string = first
            substitute = second
            if sub_string in psrd:
                psrd = psrd.replace(sub_string, substitute)
                print(psrd)
            else:
                print("Nothing to replace!")
    command = input()
print(f"Your password is: {psrd}")