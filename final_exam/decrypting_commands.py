string = input()

while True:
    command = input()
    if command == "Finish":
        break
    splitted = command.split(" ")
    if splitted[0] == "Replace":
        current_char = splitted[1]
        new_char = splitted[2]
        string = string.replace(current_char, new_char)
        print(string)
    if splitted[0] == "Cut":
        start_index = int(splitted[1])
        end_index = int(splitted[2])
        if (len(string) - 1) < start_index or (len(string) - 1) < end_index:
            print("Invalid indices!")
        else:
            string = string.replace(string[start_index:end_index + 1], "")
            print(string)
    if splitted[0] == "Make":
        upper_or_lower = splitted[1]
        if upper_or_lower == "Upper":
            string = string.upper()
        elif upper_or_lower == "Lower":
            string = string.lower()
        print(string)
    if splitted[0] == "Check":
        string_to_be_checked = splitted[1]
        if string_to_be_checked in string:
            print(f"Message contains {string_to_be_checked}")
        else:
            print(f"Message doesn't contain {string_to_be_checked}")
    if splitted[0] == "Sum":
        start_index = int(splitted[1])
        end_index = int(splitted[2])
        if start_index < 0 or start_index > (len(string) - 1):
            print("Invalid indices!")
        elif end_index < 0 or end_index > (len(string) - 1):
            print("Invalid indices!")
        else:
            substring = string[start_index:end_index+1]
            sum = 0
            for letter in substring:
                sum += int(ord(letter))
            print(sum)

