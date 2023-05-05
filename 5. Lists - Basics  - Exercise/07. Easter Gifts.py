presents = input().split(" ")
command = ""
gift_status = ""
gift_value = ""

while command != "No Money":
    command = input()
    gift_status, *gift_value = command.split()          # since command can have 2 or 3 elements, use * to catch everything after the first "interval"
    if gift_status == "OutOfStock":
        if gift_value[0] in presents:
            for i in range(len(presents)):
                if presents[i] == gift_value[0]:
                    presents[i] = "None"

    elif gift_status == "Required":                     # in this case gift_value is a list with {gift}, {index}
        if int(gift_value[1]) < len(presents):
            value_change_index = int(gift_value[1])
            presents.pop(value_change_index)
            presents.insert(value_change_index, gift_value[0])
        elif int(gift_value[1]) == len(presents):
            presents.pop()
            presents.append(gift_value[0])

    elif gift_status == "JustInCase":
        presents.pop()
        presents.append(gift_value[0])

for value in presents:
    if value != "None":
        print(value, end=" ")

# inputs below___________________________

# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money

# Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
# Required Paper 8
# OutOfStock Clothes
# Required Chocolate 2
# JustInCase Hat
# OutOfStock Cable
# No Money
