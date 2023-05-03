user_input = input()

lst_new = user_input.split(" ")
reversed_list = []

for value in lst_new:
    value = int(value) * -1
    reversed_list.append(value)

print(reversed_list)
