#
#
# def all_chars_in_between(char1, char2):
#     list_of_chars = []
#     for character in range(ord(char1) + 1, ord(char2)):
#         list_of_chars.append(chr(character))
#     list_to_string = ""
#     for chr_index in range(len(list_of_chars)):
#         list_to_string += list_of_chars[chr_index] + " "
#     return list_to_string[0:-1]
#
# first_character = input()
# second_character = input()
# print(all_chars_in_between(first_character, second_character))



def all_chars_in_between(char1, char2):
    list_of_chars = []
    for character in range(ord(char1) + 1, ord(char2)):
        list_of_chars.append(chr(character))
    return list_of_chars

first_character = input()
second_character = input()
result = all_chars_in_between(first_character, second_character)
print(" ".join(result))
