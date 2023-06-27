import re

main_string = input()

pattern = re.compile(
    r"(^|(?<=\s))([A-Za-z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*(\b|(?=\s))")
result = re.finditer(pattern, main_string)
for show in result:
    print(show[0])