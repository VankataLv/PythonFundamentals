start = int(input())
end = int(input())

for i_ascii in range(start, end + 1):
    print(f"{chr(i_ascii)}" , end=" ")
