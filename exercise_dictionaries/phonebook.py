phonebook = {}

while True:
    line = input().split("-")
    if len(line) < 2:
        searching_count = int(line[0])
        break
    name = line[0]
    phone_number = line[1]
    phonebook[name] = phone_number

for searched_name in range(searching_count):
    current_name = input()
    if current_name in phonebook.keys():
        print(f"{current_name} -> {phonebook[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")

