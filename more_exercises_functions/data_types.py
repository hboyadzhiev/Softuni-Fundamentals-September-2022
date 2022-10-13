def data_type(string, number):
    if string == "int":
        return int(number) * 2
    elif string == "real":
        result = float(number) * 1.5
        return f"{result:.2f}"
    return f"${number}$"

current_string = input()
current_number = input()
print(data_type(current_string, current_number))