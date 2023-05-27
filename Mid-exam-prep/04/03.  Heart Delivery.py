neighbourhood = list(map(int, input().split("@")))
cupid_pos = 0
command = input()

while command != "Love!":
    action, length = command.split(" ")
    length = int(length)
    cupid_pos += length                                           # jumping phase
    if cupid_pos >= len(neighbourhood):                        # if cupid goes outside the neighbourhood
        cupid_pos = 0
    if neighbourhood[cupid_pos] == 0:                             # if house does not need any more hearts
        print(f"Place {cupid_pos} already had Valentine's day.")
    else:
        neighbourhood[cupid_pos] -= 2
        if neighbourhood[cupid_pos] == 0:
            print(f"Place {cupid_pos} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {cupid_pos}.")
houses_with_hearts = 0
for value in neighbourhood:
    if value > 0:
        houses_with_hearts += 1

if houses_with_hearts == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {houses_with_hearts} places.")
