import re
from math import floor
cur_item = {}
txt = input()
lst_calories = []
calories = 0
pattern = r"(?P<sep>\||#)(?P<name>[A-Za-z\s]+)(\1)(?P<expdate>\d{2}/\d{2}/\d{2})(\1)(?P<calories>\d+)(\1)"
food_stores = re.finditer(pattern, txt)
lst_calories = re.findall(pattern, txt)
for i in lst_calories:
    calories += int(i[5])
print(f"You have food to last you for: {floor(calories / 2000)} days!")
for item in food_stores:
    cur_item = item.groupdict()
    print(f"Item: {cur_item['name']}, Best before: {cur_item['expdate']}, Nutrition: {cur_item['calories']}")

# #Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|