import re
text = input()
the_word = input()
pattern = fr"\b{the_word}\b"
matches = re.findall(pattern, text, re.IGNORECASE)
print(len(matches))