given_string = input()
digits = ""
letters = ""
other_symbols = ""

for symbol in given_string:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        other_symbols += symbol
print(digits)
print(letters)
print(other_symbols)