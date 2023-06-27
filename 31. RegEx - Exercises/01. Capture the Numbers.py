import re
pattern = r"[0-9]+"
text = input()
while text:
    matches = [print(el, end=" ")for el in re.findall(pattern, text)]
    text = input()

# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45

