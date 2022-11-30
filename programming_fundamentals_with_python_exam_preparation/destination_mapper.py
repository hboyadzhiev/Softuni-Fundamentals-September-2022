import re

string = input()
travel_points = 0
destinations = []
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

matches = re.findall(pattern, string)
for destination in matches:
    destinations.append(destination[1])
    travel_points += len(destination[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")


