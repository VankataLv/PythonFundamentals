import re

pattern = r"((www)\.([A-Za-z0-9\-]+)\.([a-z]+[a-z\.\-]+))"
txt = input()
while txt:
    match = re.findall(pattern, txt)
    if match:
        print(match[0][0])
    txt = input()
