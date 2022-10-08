def absolute_value(some_string):
    final_list = []
    string_to_list = some_string.split(" ")
    for num in string_to_list:
        final_list.append(abs(float(num)))
    return final_list


string = input()
print(absolute_value(string))