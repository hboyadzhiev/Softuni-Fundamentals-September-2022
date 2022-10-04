first_line = input().split(" ")
second_line = input()

second_line_into_list = []
second_line_into_list.extend(second_line)

message = []
current_index = 0

for sequence_index in range(len(first_line)):
    for nums in first_line[sequence_index]:
        current_index += int(nums)
    if current_index < len(second_line_into_list):
        message.append(second_line_into_list[current_index])
        second_line_into_list.remove(second_line_into_list[current_index])
    else:
        current_index = (current_index % len(second_line_into_list))
        message.append(second_line_into_list[current_index])
        second_line_into_list.remove(second_line_into_list[current_index])
    current_index = 0

message_into_string = ""
for letter_index in range(len(message)):
    message_into_string += str(message[letter_index])

print((message_into_string))