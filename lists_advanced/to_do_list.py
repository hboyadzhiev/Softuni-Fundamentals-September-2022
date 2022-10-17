to_do_list = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    splitted = command.split("-")
    priority_into_index = int(splitted[0]) - 1
    note = splitted[1]
    to_do_list.pop(priority_into_index)
    to_do_list.insert(priority_into_index, note)

non_zero_result = [noted for noted in to_do_list if noted != 0]
print(non_zero_result)