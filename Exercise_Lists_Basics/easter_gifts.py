gifts_list = input().split()
command = input()

while command != "No Money":
    if "OutOfStock" in command:
        gift_to_be_replaced = command[11:]
        for gift_index in range(len(gifts_list)):
            if gifts_list[gift_index] == gift_to_be_replaced:
                gifts_list[gift_index] = "None"
    elif "Required" in command:
        command_list = command.split()
        if 0 <= int(command_list[2]) <= (len(gifts_list) - 1):
            gifts_list[int(command_list[2])] = command_list[1]
    elif "JustInCase" in command:
        command_list = command.split()
        gifts_list[-1] = command_list[1]
    command = input()

while "None" in gifts_list:
    gifts_list.remove("None")

print(*gifts_list, sep = " ")