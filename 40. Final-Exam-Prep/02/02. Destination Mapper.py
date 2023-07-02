import re
destinations = []
txt = input()
pattern = r"(?P<sep>=|/)(?P<destination>[A-Z]{1}[A-Za-z]{2,})(\1)"
points = 0
matches = re.findall(pattern, txt)
for match in matches:
    destinations.append(match[1])
for destination in destinations:
    points += len(destination)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
