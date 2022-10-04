line = input().split(", ")
zero_counter = 0
string_to_integers = []

while "0" in line:
    line.remove("0")
    zero_counter += 1

for zero in range(zero_counter):
    line.append("0")
for number_index in range(len(line)):
    string_to_integers.append(int(line[number_index]))

print(string_to_integers)
