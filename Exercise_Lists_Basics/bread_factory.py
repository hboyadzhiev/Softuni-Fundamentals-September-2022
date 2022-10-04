events = input().split("|")
current_energy = 100
gained_energy = 0
coins = 100
all_events_handled = True

for event_index in range(len(events)):
    splitted_event = events[event_index].split("-")
    name_or_event = splitted_event[0]
    current_number = int(splitted_event[1])
    if name_or_event == "rest":
        if current_energy + current_number <= 100:
            gained_energy = current_number
            current_energy += current_number
        else:
            gained_energy = 100 - current_energy
            current_energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif name_or_event == "order":
        if current_energy >= 30:
            coins += current_number
            current_energy -= 30
            print(f"You earned {current_number} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        if coins >= current_number:
            print(f"You bought {name_or_event}.")
            coins -= current_number
        else:
            print(f"Closed! Cannot afford {name_or_event}.")
            all_events_handled = False
            break

if all_events_handled:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")

