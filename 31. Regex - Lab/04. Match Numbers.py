import re
text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, text)
matches = [num.group() for num in matches]
print(*matches)
