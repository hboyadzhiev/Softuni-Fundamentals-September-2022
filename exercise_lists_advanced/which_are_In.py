sequence_1 = input().split(", ")
sequence_2 = input()
new_list = [str for str in sequence_1 if str in sequence_2]
print(new_list)


