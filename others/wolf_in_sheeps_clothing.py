# Exercise: Wolves have been reintroduced to Great Britain. You are a sheep farmer and
# are now plagued by wolves who pretend to be sheep. Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue, which is
# at the end of the list: [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep".
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!"
# where N is the sheep's position in the queue. Note: there will always be exactly
# one wolf on the list
# Input
# The input will be a single string containing the animals separated by
# a comma and a single space ", "

from re import split

a = input()
list = a.split(", ")
number_of_words = len(list)

for index, value in enumerate(list):
  if index - number_of_words == -1 and value == "wolf":
    print("Please go away and stop eating my sheep")
  elif value == "wolf":
    position_of_wolf = number_of_words - index
    position_of_sheep = position_of_wolf - 1
    print(f"Oi! Sheep number {position_of_sheep}! You are about to be eaten by a wolf!")