lines_count = int(input())
word = input()
strings = []
filtered_strings = []

for strngs in range(lines_count):
    string = input()
    strings.append(string)
print(strings)

for index, filtered_string in enumerate(strings):
    if word in filtered_string:
        filtered_strings.append(strings[index])
print(filtered_strings)


