n = int(input())
dict_syns = {}
for i in range(n):
    word = input()
    synonym = input()
    if word in dict_syns:
        dict_syns[word].append(synonym)
    else:
        dict_syns[word] = []
        dict_syns[word].append(synonym)
for word in dict_syns:
    print(f"{word} - {', '.join(dict_syns[word])}")

# 3
# cute
# adorable
# cute
# charming
# smart
# clever
#---------------
# 2
# task
# problem
# task
# assignment
