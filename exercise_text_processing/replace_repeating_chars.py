string = input()
final_string = ""
current_symbol= ""
for symbol in string:
    if symbol != current_symbol:
        final_string += symbol
        current_symbol = symbol

print(final_string)
