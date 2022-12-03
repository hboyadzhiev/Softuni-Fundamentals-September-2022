all_stops = input()

while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {all_stops}")
        break
    else:
        splitted = command.split(":")
        if splitted[0] == "Add Stop":
            index = int(splitted[1])
            string = splitted[2]
            if 0 <= index < len(all_stops):
                all_stops = all_stops[:index] + string + all_stops[index:]
        elif splitted[0] == "Remove Stop":
            start_index = int(splitted[1])
            end_index = int(splitted[2])
            if 0 <= start_index <= end_index < len(all_stops):
                all_stops = all_stops.replace(all_stops[start_index:end_index + 1], "")
        elif splitted[0] == "Switch":
            old_string = splitted[1]
            new_string = splitted[2]
            if old_string in all_stops:
                all_stops = all_stops.replace(old_string, new_string)
    print(all_stops)






