given_string = input()
final_string = ""
for symbol in given_string:
    final_string += chr(ord(symbol) + 3)
print(final_string)