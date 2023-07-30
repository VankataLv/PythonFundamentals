import re

pattern = r"!([A-Z]{1}[a-z]{2,})!:\[([A-Za-z]{8,})\]"
n = int(input())
for line in range(n):
    txt = input()
    valid_cmd = re.findall(pattern, txt)
    if valid_cmd:
        cmd, msg = valid_cmd[0][0], valid_cmd[0][1]
        lst_values = []
        for char in msg:
            lst_values.append(str(ord(char)))
        print(f"{cmd}: {' '.join(lst_values)}")
    else:
        print("The message is invalid")

# 3
# go:[outside]
# !drive!:YourCarToACarWash
# !Watch!:[LordofTheRings]