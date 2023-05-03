key = int(input())
number_lines = int(input())

for line in range(number_lines):
    char = input()
    print(chr(ord(char) + key), end="")
