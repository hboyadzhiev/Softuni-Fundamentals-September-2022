number_of_lines = int(input())

balanced = False
opening_bracket = False

for expressions in range(number_of_lines):
    line = input()
    if line == "(":
        if opening_bracket == True:
            break
        else:
            opening_bracket = True
    if line == ")":
        if opening_bracket == False:
            break
        else:
            balanced = True
            opening_bracket = False


if balanced == False:
    print("UNBALANCED")
else:
    print("BALANCED")


