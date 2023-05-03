factor = int(input())
count = int(input())
multiple_list = []

for number in range(1, count + 1):
    multiple_list.append(number * factor)

print(multiple_list)