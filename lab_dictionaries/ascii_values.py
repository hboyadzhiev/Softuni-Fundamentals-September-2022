char_list = input().split(", ")
characters = {key: ord(key) for key in char_list}
print(characters)