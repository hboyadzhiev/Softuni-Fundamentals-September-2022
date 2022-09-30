lines_count = int(input())

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

lst = []

for numbers in range(lines_count):
    current_number = int(input())
    lst.append(current_number)
command = input()

filtered_numbers = []

for nums in lst:
    filter_passes = (
        (command == COMMAND_EVEN and nums % 2 == 0) or
        (command == COMMAND_ODD and nums % 2 != 0) or
        (command == COMMAND_POSITIVE and nums >= 0) or
        (command == COMMAND_NEGATIVE and nums < 0)
    )
    if filter_passes:
        filtered_numbers.append(nums)
print(filtered_numbers)


