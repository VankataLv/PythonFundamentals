import re
pattern = r"\b(?P<day>[0-9]{2})([-.\/])(?P<month>[A-Z]{1}[a-z]{2})\2(?P<year>[0-9]{4})\b"
text = input()
valid_dates = re.findall(pattern,text)
for el in valid_dates:
    print(f"Day: {el[0]}, Month: {el[2]}, Year: {el[3]}")
