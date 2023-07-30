txt = input()
command = input()
while command != "Travel":
    action, first_el, second_el = command.split(":")
    if action == "Add Stop":
        ind = int(first_el)
        if ind in range(0, len(txt)):
            first_part = txt[:ind]
            second_part = txt[ind:]
            txt = first_part + second_el + second_part
    elif action == "Remove Stop":
        start_index = int(first_el)
        end_index = int(second_el)
        if start_index in range(0, len(txt)) and end_index in range(0, len(txt)):
            first_part = txt[:start_index]
            second_part = txt[end_index + 1:]
            txt = first_part + second_part
    elif action == "Switch":
        old_str = first_el
        new_str = second_el
        if old_str in txt:
            txt = txt.replace(old_str, new_str)
    print(txt)
    command = input()
print(f"Ready for world tour! Planned stops: {txt}")
