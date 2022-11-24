given_string = input()
final_string = ""
explosion = 0
for index in range(len(given_string)):
    if explosion > 0 and given_string[index] != ">":
        explosion -= 1
    elif given_string[index] == ">":
        final_string += given_string[index]
        explosion += int(given_string[index + 1])
    else:
        final_string += given_string[index]
print(final_string)


