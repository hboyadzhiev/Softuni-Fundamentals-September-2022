countries = input().split(", ")
cities = input().split(", ")
our_dictionary = {countries[index]: cities[index] for index in range(len(countries))}
for key, value in our_dictionary.items():
    print(f"{key} -> {value}")

