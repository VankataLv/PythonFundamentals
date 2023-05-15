ascen_order_todo = [0] * 10
to_do_command = input()

while to_do_command != "End":
    importance, note = to_do_command.split("-")
    ascen_order_todo[int(importance) - 1] = note
    to_do_command = input()

print([element for element in ascen_order_todo if not element == 0])
