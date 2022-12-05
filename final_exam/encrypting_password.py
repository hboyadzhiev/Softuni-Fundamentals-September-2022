import re
passwords_count = int(input())
for line in range(passwords_count):
    current_line = input()
    pattern = r"(.+)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})\<\1"
    match = re.findall(pattern, current_line)
    if match:
        concatenated = ""
        concatenated += (match[0][1] + match[0][2] + match[0][3] + match[0][4])
        print(f"Password: {concatenated}")
    else:
        print("Try another password!")