# Exercise: Write a program that takes a single string and prints a list of all the capital
# letters indices.

string = input()

capitals_list = []

for count, value in enumerate(string):
  if value.isupper() == True:
    capitals_list.append(count)

print(capitals_list)