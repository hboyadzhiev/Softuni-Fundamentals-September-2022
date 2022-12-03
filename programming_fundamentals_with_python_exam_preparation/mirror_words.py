import re

string = input()
mirror_words = []
pattern = r"([\#\@])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)"
matches = re.findall(pattern, string)
pairs_count = len(matches)
if pairs_count == 0:
    print("No word pairs found!")
else:
    print(f"{pairs_count} word pairs found!")
    for match in matches:
        if match[1] == match[3][::-1]:
            mirror_words.append(f"{match[1]} <=> {match[3]}")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))




























