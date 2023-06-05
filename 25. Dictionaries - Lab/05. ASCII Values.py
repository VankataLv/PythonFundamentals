char_lst = input().split(", ")
chr_dct = {el: ord(el) for el in char_lst}
print(chr_dct)

# print({el: ord(el) for el in input().split(", ")})
