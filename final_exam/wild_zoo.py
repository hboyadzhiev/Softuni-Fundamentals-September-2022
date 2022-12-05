areas = {}
while True:
    line = input()
    if line == "EndDay":
        break
    splitted = line.split(": ")
    if splitted[0] == "Add":
        splitted_1 = splitted[1].split("-")
        animal_name, needed_food, area = splitted_1[0], int(splitted_1[1]), splitted_1[2]

        if area not in areas.keys():
            areas[area] = {}
        if animal_name not in areas[area].keys():
            areas[area][animal_name] = needed_food
        else:
            areas[area][animal_name] += needed_food

    elif splitted[0] == "Feed":
        splitted_2 = splitted[1].split("-")
        animal_name, food = splitted_2[0], int(splitted_2[1])
        for current_area in areas.keys():
            if animal_name in current_area:
                current_area[animal_name] -= food
                if current_area[animal_name] <= 0:
                    print(f"{animal_name} was successfully fed")
                    del current_area[animal_name]

print(areas)
hungry_animals = []
areas_with_hungry_animals = []

for current_area in areas:
    for current_animal, value in current_area.items():
        if value > 0:
            hungry_animals.append(f"{current_animal} -> {value}")
            if current_area not in areas_with_hungry_animals:
                areas_with_hungry_animals.append(current_area)
if len(hungry_animals) > 0:
    print("Animals")
    for the_animal in hungry_animals:
        print(f" {the_animal}\n")
    print("Areas with hungry animals:")
    for the_area in areas_with_hungry_animals:
        print(f" {the_area}: {len(areas[the_area])}")