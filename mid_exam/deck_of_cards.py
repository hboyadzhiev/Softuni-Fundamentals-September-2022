list_of_cards = input().split(", ")
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split(", ")
    if current_command[0] == "Add":
        card = current_command[1]
        if card not in list_of_cards:
            list_of_cards.append(card)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    if current_command[0] == "Remove":
        card = current_command[1]
        if card in list_of_cards:
            list_of_cards.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")
    if current_command[0] == "Remove At":
        if 0 <= int(current_command[1]) < len(list_of_cards):
            index = int(current_command[1])
            list_of_cards.remove(list_of_cards[index])
            print("Card successfully removed")
        else:
            print("Index out of range")
    if current_command[0] == "Insert":
        if 0 <= int(current_command[1]) < len(list_of_cards):
            index = int(current_command[1])
            card = current_command[2]
            if card in list_of_cards:
                print("Card is already added")
            else:
                list_of_cards.insert(index, card)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(list_of_cards))