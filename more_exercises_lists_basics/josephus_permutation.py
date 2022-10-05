
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