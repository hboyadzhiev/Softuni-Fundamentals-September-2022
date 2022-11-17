strings = input().split(" ")
string1 = strings[0]
string2 = strings[1]
total_sum = 0

if len(string1) > len(string2):
    for index in range(len(string2)):
        total_sum += ord(string1[index]) * ord(string2[index])
    for next_index in range(len(string1) - len(string2)):
        total_sum += ord(string1[next_index + len(string2)])

elif len(string1) < len(string2):
    for index in range(len(string1)):
        total_sum += ord(string1[index]) * ord(string2[index])
    for next_index in range(len(string2) - len(string1)):
        total_sum += ord(string2[next_index + len(string1)])

else:
    for index in range(len(string1)):
        total_sum += ord(string1[index]) * ord(string2[index])

print(total_sum)


