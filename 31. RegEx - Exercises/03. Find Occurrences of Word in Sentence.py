import re
text = input().lower()
word = input().lower()
pattern = rf"\b{word}\b"
result = re.findall(pattern, text)
print(len(result))
