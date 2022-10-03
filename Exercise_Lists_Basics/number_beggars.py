string = input().split(", ")
beggars_count = int(input())

string_into_integers = []
for nums in string:
    string_into_integers.append(int(nums))

all_results = []
starting_index = 0

while starting_index < beggars_count:
    sum_for_one_beggar = 0
    for indx in range(starting_index, len(string), beggars_count):
        received_sum = string_into_integers[indx]
        sum_for_one_beggar += received_sum
    all_results.append(sum_for_one_beggar)
    starting_index += 1

print(all_results)

