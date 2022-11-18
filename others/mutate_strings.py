#
# Exercise: You will be given two strings. Transform the first string into the second one,
# letter by letter, starting from the first one. After each interaction,
# print the resulting string only if it is unique.
# Note: the strings will have the same length.

first_string = input()
second_string = input()

new_mutated_string = first_string


for letter in range(len(first_string)):
  left_side = second_string[0:letter+1]
  right_side = first_string[letter+1:len(first_string)]
  mutated_string = left_side + right_side
  if mutated_string == new_mutated_string:
    continue
  print(mutated_string)
  new_mutated_string = mutated_string