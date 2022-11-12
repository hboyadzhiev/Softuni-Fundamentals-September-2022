inptt = input().lower()
line = inptt.split(" ")
junk_items = {}
main_items = {"shards": 0, "fragments": 0, "motes": 0}

item_obtained = False

for index in range(0, len(line), 2):
    quantity = int(line[index])
    item = line[index + 1]
    if item not in main_items.keys():
        if item not in junk_items.keys():
            junk_items[item] = 0
        junk_items[item] += quantity
    else:
        main_items[item] += quantity
        if main_items[item] >= 250:
            if item == "shards":
                print("Shadowmourne obtained!")
            elif item == "fragments":
                print("Valanyr obtained!")
            elif item == "motes":
                print("Dragonwrath obtained!")
            main_items[item] -= 250
            item_obtained = True
            if item_obtained == True:
                break
    if item_obtained == True:
        break
for key, value in main_items.items():
    print(f"{key}: {value}")
for key, value in junk_items.items():
    print(f"{key}: {value}")








