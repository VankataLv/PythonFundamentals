class Party:
    def __init__(self):
        self.people = []


my_party = Party()
command = input()
while command != "End":
    my_party.people.append(command)
    command = input()

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")
