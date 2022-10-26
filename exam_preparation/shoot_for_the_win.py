targets = input().split(" ")
target_sequence = [int(x) for x in targets]
count_of_shot_targets = 0

def if_bigger_smaller(some_integer):
    if some_integer > current_target and some_integer != -1:
        some_integer -= current_target
    elif some_integer <= current_target and some_integer != -1:
        some_integer += current_target
    return some_integer

while True:
    command = input()
    if command == "End":
        break
    current_index = int(command)
    current_target = 0
    if current_index < len(target_sequence):
        if target_sequence[current_index] != -1 and -1 < current_index:
            count_of_shot_targets += 1
            current_target = int(target_sequence[current_index])
            target_sequence[current_index] = -1
            target_sequence = list(map(if_bigger_smaller, target_sequence))

int_into_strings = [str(x) for x in target_sequence]
print(f"Shot targets: {count_of_shot_targets} -> {' '.join(int_into_strings)}")