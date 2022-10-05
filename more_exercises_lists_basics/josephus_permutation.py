# sequence = input().split(" ")
# step = int(input())
# executed_list = []
# current_index = 0
#
# if step > len(sequence):
#     current_index = (step % len(sequence)) - 1
# else:
#     current_index = step - 1
#
# while len(sequence) != 0:
#     executed_list.append(int(sequence[current_index]))
#     sequence.remove((sequence[current_index]))
#     if len(sequence) == 0:
#         break
#     elif len(sequence) == 1:
#         current_index = 0
#     else:
#         if step == 1:
#             current_index += 1
#         else:
#             current_index += step - 1
#     if current_index > (len(sequence) - 1):
#         current_index = (current_index % (len(sequence)))
#         if current_index > (len(sequence) - 1):
#             if step % 2 == 0:
#                 current_index = 1
#             else:
#                 current_index = 0
#
# list_without_spaces = str(executed_list).replace(" ", "")
# print(list_without_spaces)


# circle = [int(number) for number in input().split()]
# kill_count = int(input())
# result = list()
# counter = 0
#
# index = 0
# while len(circle) > 0:
#     counter += 1
#
#     if counter % kill_count == 0:
#         result.append(circle.pop(index))
#     elif counter % kill_count != 0:
#         index += 1
#
#     if index >= len(circle):
#         index = 0
#
#
# print(str(result).replace(' ', ''))


soldiers = [int(number) for number in input().split()]
step = int(input())
executed_list = list()
counter = 0
index = 0

while len(soldiers) > 0:
    counter += 1
    if counter % step == 0:
        executed_list.append(soldiers.pop(index))

    elif counter % step != 0:
        index += 1
    if index >= len(soldiers):
        index = 0

print(str(executed_list).replace(" ", ""))