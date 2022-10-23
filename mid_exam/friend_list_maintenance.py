usernames = tuple(input().split(", "))
usernames_list = list(usernames)
blacklisted_counter = 0
errors_counter = 0
while True:
    command = input()
    if command == "Report":
        break
    splitted_command = command.split(" ")
    if splitted_command[0] == "Blacklist":
        name = splitted_command[1]
        if name in usernames_list:
            index = usernames.index(name)
            usernames_list[index] = "Blacklisted"
            blacklisted_counter += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif splitted_command[0] == "Error":
        name = splitted_command[1]
        index = int(splitted_command[1])
        if 0 <= index < len(usernames_list):
            name = usernames_list[index]
            if name != "Blacklisted" and name != "Lost":
                usernames_list[index] = "Lost"
                print(f"{name} was lost due to an error.")
                errors_counter += 1
    elif splitted_command[0] == "Change":
        index = int(splitted_command[1])
        if 0 <= index < len(usernames_list):
            new_name = splitted_command[2]
            name = usernames_list[index]
            usernames_list[index] = new_name
            print(f"{name} changed his username to {new_name}.")
print(f"Blacklisted names: {blacklisted_counter}")
print(f"Lost names: {errors_counter}")
print(" ".join(usernames_list))

