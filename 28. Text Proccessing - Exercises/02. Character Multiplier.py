first, second = input().split()
l_1 = len(first)
l_2 = len(second)
total_sum = 0

if l_1 == l_2:
    for i in range(l_1):
        total_sum += ord(first[i]) * ord(second[i])
elif l_1 > l_2:
    for i in range(l_2):
        total_sum += ord(first[i]) * ord(second[i])
    diff = l_1 - l_2
    for i in range(diff):  # 0,1,2,3...
        total_sum += ord(first[-1-i])
elif l_1 < l_2:
    for i in range(l_1):
        total_sum += ord(first[i]) * ord(second[i])
    diff = l_2 - l_1
    for i in range(diff):
        total_sum += ord(second[-1 - i])
print(total_sum)
