import re

pattern_letters = r"[A-Za-z]"
pattern_nums = r"\d"
participants = input().split(", ")
results_by_name = {}
results_by_distance = {}
lst_ordered_distances = []
cmd = input()
while cmd != "end of race":
    letters_lst = re.findall(pattern_letters, cmd)
    nums_lst = re.findall(pattern_nums, cmd)
    name = ""
    distance = 0
    for char in letters_lst:
        name += char
    if name in participants:
        for digit in nums_lst:
            digit = int(digit)
            distance += digit
        if name in results_by_name:
            results_by_name[name] += distance
        else:
            results_by_name[name] = distance
    cmd = input()
for key, value in results_by_name.items():
    results_by_distance[value] = key
    lst_ordered_distances.append(value)
lst_ordered_distances.sort(reverse=True)
places_names = {'1st place': results_by_distance[lst_ordered_distances[0]],
                '2nd place': results_by_distance[lst_ordered_distances[1]],
                '3rd place': results_by_distance[lst_ordered_distances[2]]}
for key, value in places_names.items():
    print(f"{key}: {value}")
