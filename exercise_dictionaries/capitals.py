countries = input().split(", ")
cities = input().split(", ")
# our_dictionary = {countries[index]: cities[index] for index in range(len(countries))}
our_dictionary = {country: city for country, city in zip(countries, cities)}
for key, value in our_dictionary.items():
    print(f"{key} -> {value}")

