def rounding(string):
    list = []
    for number in string:
        list.append(round(float(number)))
    return list

current_string = input().split(" ")
print(rounding(current_string))