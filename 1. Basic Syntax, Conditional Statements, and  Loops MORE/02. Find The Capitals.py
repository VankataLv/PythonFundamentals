my_list = list(input())
capital_indices = []
for i in range(len(my_list)):
    if 65 <= ord(my_list[i]) <= 90:
        capital_indices.append(i)
print(capital_indices)
