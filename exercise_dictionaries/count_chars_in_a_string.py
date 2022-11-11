current_string = "".join(input().split(" "))
letters_dictionary = {}

for letter in current_string:
    if letter not in letters_dictionary.keys():
        letters_dictionary[letter] = 0
    letters_dictionary[letter] += 1

for key, value in letters_dictionary.items():
    print(f"{key} -> {value}")