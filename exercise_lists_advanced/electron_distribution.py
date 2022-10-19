electrons_number = int(input())
filled_shells_list = []
n = 1
while electrons_number >= 2 * n ** 2:
    filled_shells_list.append(2 * n ** 2)
    electrons_number -= 2 * n ** 2
    n += 1
filled_shells_list.append(electrons_number)
print(filled_shells_list)

