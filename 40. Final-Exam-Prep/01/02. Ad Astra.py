import re
from math import floor
cur_item = {}
txt = input()
lst_calories = []
calories = 0
pattern = r"(\||#)(?P<name>[A-Za-z\s]+)(\||#)(?P<expdate>\d{2}/\d{2}/\d{2})(\||#)(?P<calories>\d+)(\||#)"
pattern2 = r"(\||#)([A-Za-z\s]+)(\||#)(?P<expdate>\d{2}/\d{2}/\d{2})(\||#)(?P<calories>\d+)(\||#)"
food_stores = re.finditer(pattern, txt)
lst_calories = re.findall(pattern, txt)
for i in lst_calories:
    calories += int(i[5])
print(f"You have food to last you for: {floor(calories / 2000)} days!")
for item in food_stores:
    cur_item = item.groupdict()
    print(f"Item: {cur_item['name']}, Best before: {cur_item['expdate']}, Nutrition: {cur_item['calories']}")
