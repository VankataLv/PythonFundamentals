import re
pattern = r"(?P<day>\d{2})(?P<separator>[/.\s/-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
txt = input()
valid_dates = re.finditer(pattern, txt)
for date in valid_dates:
    cur_date = date.groupdict()
    print(f"Day: {cur_date['day']}, Month: {cur_date['month']}, Year: {cur_date['year']}")

