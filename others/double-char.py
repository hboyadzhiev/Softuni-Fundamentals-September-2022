# Exercise You will be given strings until you receive the command "End".
# For each string given, you should print a string in which each character
# (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!

command = input()
doubled_word = ""

while command != "End":
  if command != "SoftUni":
    for letter in command:
      doubled_word += letter * 2
    print(doubled_word)
  doubled_word = ""
  command = input()
