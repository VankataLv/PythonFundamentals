data = input().split(" ")
command = input()
new_value = ""
while command != "3:1":
    if command[0:5] == "merge":
        action, start_index, end_index = command.split(" ")
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index not in range(0, len(data)) or end_index not in range(0, len(data)):
            if start_index > len(data) - 1:
                start_index = end_index = len(data) - 1
            elif end_index > len(data) - 1:
                end_index = len(data) - 1
        for i_to_merge in range(start_index, end_index + 1):
            new_value += data[i_to_merge]
        for i_to_delete in range(end_index, start_index - 1, -1):
            data.pop(i_to_delete)
        data.insert(0, new_value)
        new_value = ""
        print(data)
    elif command[0:6] == "divide":
        action, index, partitions = command.split(" ")
    command = input()

# Ivo Johny Tony Bony Mony
# merge 0 3
# merge 3 4
# merge 0 3
# 3:1
