data = input().split(" ")

def merge(data_copied, some_command):
    if len(data_copied) - 1 < int(some_command[1]):
        return data_copied
    data_copy = [x for x in data_copied]
    concatenated_list = []
    if len(data_copied) - 1 < int(some_command[2]):
        for current_index in range(int(some_command[1]), len(data_copied)):
            concatenated_list += str(data_copied[current_index])
            del data_copy[current_index]
        list_into_string = "".join(concatenated_list)
        new_list = data_copy.append(list_into_string)
    else:
        for current_index in range(int(some_command[1]), some_command[2]):
            concatenated_list += str(data_copied[current_index])
            del data_copy[current_index]
        list_into_string = "".join(concatenated_list)
        new_list = data_copy.insert(int(some_command[1]), list_into_string)
    return new_list

def divide(a_command):


while True:
    command = input().split()
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        pass
    # tuka nakraja kato priemesh ot funkcijata returna, zadaj data.clear() i data = new_list(returna ot funkcijata)
    elif command[0] == "divide":
        pass
#


# list = [1, 2, 3, 4, 5]
# list_copy = list
# list_copy.remove(2)
# print(list)
# print(list_copy)
#
# list_copy_two = [x for x in list]
# print(list_copy_two)
# list_copy_two.remove(5)
# print(list_copy_two)
# print(list)

# list = [1, 2, 3, 4, 5]
# del list[2:4]
# print(list)
# list.insert(2, "macka")
# print(list)

# list = [1, 2, 3, 4]
# new_list = []
# for i_index in range(2, 4):
#     new_list += str(list[i_index])
# list_into_string = "".join(new_list)

