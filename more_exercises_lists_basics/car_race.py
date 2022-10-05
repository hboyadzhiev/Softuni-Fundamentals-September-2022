sequence = input().split(" ")

current_time = 0
total_time_left = 0
total_time_right = 0

for left_part_index in range(len(sequence) // 2):
    current_time += int(sequence[left_part_index])
    if int(sequence[left_part_index]) == 0:
        current_time = current_time * 0.8
total_time_left = current_time
current_time = 0

for right_part_index in range(-1, -(len(sequence) // 2) - 1, -1):
    current_time += int(sequence[right_part_index])
    if int(sequence[right_part_index]) == 0:
        current_time = current_time * 0.8
total_time_right = current_time

if total_time_left < total_time_right:
    print(f"The winner is left with total time: {total_time_left:.1f}")
elif total_time_right < total_time_left:
    print(f"The winner is right with total time: {total_time_right:.1f}")
