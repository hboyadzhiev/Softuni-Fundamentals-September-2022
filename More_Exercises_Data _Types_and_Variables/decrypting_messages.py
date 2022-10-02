key = int(input())
lines_count = int(input())
message = ""

for letter in range(lines_count):
    current_letter = input()
    message += chr(ord(current_letter) + key)
print(message)