# Exercise: Beaches are filled with sand, water, fish, and sun. Given a string,
# calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear
# (case insensitive).

import re

string = input()
Sand = len(re.findall("Sand", string, flags=re.IGNORECASE))
Water = len(re.findall("Water", string, flags=re.IGNORECASE))
Fish = len(re.findall("Fish", string, flags=re.IGNORECASE))
Sun = len(re.findall("Sun", string,flags=re.IGNORECASE))
counter = Sand + Water + Fish + Sun
print(counter)
