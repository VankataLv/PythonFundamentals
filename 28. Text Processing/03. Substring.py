st_1 = input()
st_2 = input()
while st_1 in st_2:
    st_2 = st_2.replace(st_1, "")
print(st_2)
