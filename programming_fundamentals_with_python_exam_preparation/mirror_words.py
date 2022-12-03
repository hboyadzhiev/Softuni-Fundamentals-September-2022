import re
string = input()
pattern = r"([\#\@])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)"
matches = re.findall(pattern, string)
for match in matches:
    