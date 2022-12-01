number_of_pieces = int(input())
collection = {}

end = False

for piece in range(number_of_pieces):
    current_piece = input().split("|")
    piecce = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    collection[piecce] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        end = True
        break
    else:
        splitted = command.split("|")
        current_command = splitted[0]
        if current_command == "Add":
            given_piece = splitted[1]
            current_composer = splitted[2]
            current_key = splitted[3]
            if given_piece not in collection:
                collection[given_piece] = [current_composer, current_key]
                print(f"{given_piece} by {current_composer} in {current_key} added to the collection!")
            else:
                print(f"{given_piece} is already in the collection!")
        elif current_command == "Remove":
            piece_to_be_removed = splitted[1]
            if piece_to_be_removed not in collection:
                print(f"Invalid operation! {piece_to_be_removed} does not exist in the collection.")
            else:
                del (collection[piece_to_be_removed])
                print(f"Successfully removed {piece_to_be_removed}!")
        elif current_command == "ChangeKey":
            the_piece = splitted[1]
            new_key = splitted[2]
            if the_piece not in collection:
                print(f"Invalid operation! {the_piece} does not exist in the collection.")
            else:
                collection[the_piece][1] = new_key
                print(f"Changed the key of {the_piece} to {new_key}!")



for piecee, info in collection.items():
    print(f"{piecee} -> Composer: {info[0]}, Key: {info[1]}")

