import re
at_least_one_mirror_word = False
extra_print = False
txt = input()
lst_matched_words = []
pattern = r"(?P<sep>\@|\#)(?P<word>[A-Za-z]{3,})(\1)(\1)(?P<word_rev>[A-Za-z]{3,})(\1)"
matches = re.findall(pattern, txt)

if len(matches) == 0:
    print("No word pairs found!")
    print("No mirror words!")

else:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        word = match[1]
        rev_word = match[4]
        if word == rev_word[::-1]:
            at_least_one_mirror_word = True
            if not extra_print:
                print("The mirror words are:")
                extra_print = True
            lst_matched_words.append(word)
            lst_matched_words.append(rev_word)
    if not at_least_one_mirror_word:
        print("No mirror words!")
    else:
        rows_needed = len(lst_matched_words) // 2
        for i in range(0, len(lst_matched_words), 2):
            if rows_needed == 1:
                print(f"{lst_matched_words[i]} <=> {lst_matched_words[i+1]}")
                quit()
            else:
                print(f"{lst_matched_words[i]} <=> {lst_matched_words[i+1]},", end=" ")
                rows_needed -= 1
