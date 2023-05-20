secret_msg = input().split(" ")
deciphered_msg = []
num_hidden_letter = ""
rest_of_word = ""
deciphered_word = ""
for el in secret_msg:
    for ch in el:
        if ch.isnumeric():
            num_hidden_letter += ch
        else:
            rest_of_word += ch
    deciphered_word += chr(int(num_hidden_letter))           # find the first letter and add it
    deciphered_word += rest_of_word                          # add the rest of the chars
    deciphered_msg.append(deciphered_word)                   # add the deciphered word to a new list
    num_hidden_letter = rest_of_word = deciphered_word = ""  # initialize all the storages of information

for el in deciphered_msg:
    my_list = [x for x in el]
    my_list[1], my_list[-1] = my_list[-1], my_list[1]
    print("".join(my_list), end=" ")
