import re

special_letters = ["s", "t", "a", "r"]
n = int(input())
pattern = r"@([A-za-z]+)[^/@/-/!/:/>]*:(\d+)[^/@/-/!/:/>]*![^/@/-/!/:/>]*(A|D)[^/@/-/!/:/>]*!->(\d+)"
attacked_planets = []
destroyed_planets = []
for line in range(n):
    key_counter = 0
    decrypted_msg = ""
    msg = input()
    for char in msg:
        if char.lower() in special_letters:
            key_counter += 1
    for char in msg:
        decrypted_msg += chr(ord(char) - key_counter)
    data = re.findall(pattern, decrypted_msg)
    if data:
        if data[0][2] == "A":
            attacked_planets.append(data[0][0])
        elif data[0][2] == "D":
            destroyed_planets.append(data[0][0])
print(f"Attacked planets: {len(attacked_planets)}")
if attacked_planets:
    attacked_planets.sort()
    for planet in attacked_planets:
        print(f'-> {planet}')
print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    destroyed_planets.sort()
    for planet in destroyed_planets:
        print(f'-> {planet}')
# 2
# STCDoghudd4=63333$D$0A53333
# EHfsytsnhf?8555&I&2C9555SR
# 3
# tt(''DGsvywgerx>6444444444%H%1B9444
# GQhrr|A977777(H(TTTT
# EHfsytsnhf?8555&I&2C9555SR

# 80/100 in judge