num_wagons = int(input())
train = [0 for wagons in range(num_wagons)]
# train = [0] * num_wagons                     # another shorter way
command = input()

while command != "End":
    sep_command = command.split(" ")
    if sep_command[0] == "add":
        train[-1] += int(sep_command[1])
    elif sep_command[0] == "insert":
        train[int(sep_command[1])] += int(sep_command[2])
    elif sep_command[0] == "leave":
        train[int(sep_command[1])] -= int(sep_command[2])
    command = input()

print(train)
