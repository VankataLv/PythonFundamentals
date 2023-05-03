first_line = input()
money = first_line.split(", ")
beggars = int(input())
beggar_earnings = []
current_beggar_earnings = 0
old_list = list()
if len(money) > beggars:
    for beggar in range(beggars):
        for i in range(0 + beggar, len(money), len(money) // 2):
            current_beggar_earnings += int(money[i])
        beggar_earnings.insert(beggar, current_beggar_earnings)
        current_beggar_earnings = 0

elif len(money) == beggars:
    for i_value in money:
        beggar_earnings.append(int(i_value))

else:
    for i_value in money:
        old_list.append(int(i_value))
    for _ in range(0, beggars):
        beggar_earnings.append(sum(old_list[_::beggars]))
print(beggar_earnings)
