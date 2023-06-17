from math import floor
from math import ceil
data = [el for el in input().split(" ")]
command = input()
while command != "3:1":
    action, first, second = command.split(" ")
    if action == "merge":
        start_index = int(first)
        end_index = int(second)
        start_index = max(0, start_index)
        end_index = min(len(data) - 1, end_index)
        merged = ""
        for i in range(start_index, end_index + 1):
            merged += data[start_index]
            data.pop(start_index)
        data.insert(start_index, merged)
        merged = ""
    elif action == "divide":
        divided_el = []
        index = int(first)
        partitions = int(second)
        el_to_divide = data[index]
        data.pop(index)
        if len(el_to_divide) % partitions == 0:
            symbols = len(el_to_divide) // partitions
            for partition in range(partitions):
                divided_el.insert(partition, el_to_divide[0:symbols])
                el_to_divide = el_to_divide[symbols:]
            for el in reversed(divided_el):
                data.insert(index, el)
            divided_el = []
        else:
            last_el_length = ceil(len(el_to_divide) / partitions)
            other_el_length = floor(len(el_to_divide) / partitions)
            for partition in range(partitions - 1):
                divided_el.insert(partition, el_to_divide[0:other_el_length])
                el_to_divide = el_to_divide[other_el_length:]
            divided_el.append(el_to_divide)
            for el in reversed(divided_el):
                data.insert(index, el)
            divided_el = []
    command = input()

print(" ".join(data))
