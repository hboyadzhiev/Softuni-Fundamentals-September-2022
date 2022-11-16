given_string = input().split(" ")
final_string = ""
for each_str in given_string:
    final_string += each_str * len(each_str)
print(final_string)