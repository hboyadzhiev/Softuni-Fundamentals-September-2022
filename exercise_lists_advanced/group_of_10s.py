numbers = tuple(map(int, input().split(", ")))

def tens(given_numbers):
    max_value = 0
    list_copy = list(given_numbers)
    for num_index in range(10):
        max_value += 10
        current_list = []
        for number in given_numbers:
            if len(list_copy) == 0:
                break
            if (max_value - 9) <= number <= max_value:
                current_list.append(number)
                list_copy.remove(number)
        print(f"Group of {max_value}'s: {current_list}")
        if len(list_copy) == 0:
            break
    return""

result = tens(numbers)
print(result)



