version = input().split(".")
number = ((int(version[0])) * 100) + ((int(version[1])) * 10) + (int(version[2]) + 1)
if number > 999:
    number = 999
num_into_str = str(number)
print(f"{(num_into_str[0])}.{(num_into_str[1])}.{(num_into_str[2])}")