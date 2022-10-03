list_of_numbers = input().split()
count_num_to_remove = int(input())
string_to_int = []

for number in list_of_numbers:
    string_to_int.append(int(number))

for removed_num in range(count_num_to_remove):
    string_to_int.remove(min(string_to_int))
list_to_string = ""
for word in string_to_int:
    list_to_string += str(word) + ", "

print(list_to_string[0:-2])
