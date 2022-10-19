chairs_number = int(input())

free_chairs = 0
free_chairs_check = True

list_of_lists = [input().split(" ") for room in range(chairs_number)]
for room in list_of_lists:
    if len(room[0]) >= int(room[1]):
        free_chairs += len(room[0]) - int(room[1])
    else:
        print(f"{int(room[1]) - len(room[0])} more chairs needed in room {list_of_lists.index(room) + 1}")
        free_chairs_check = False

if free_chairs_check:
    print(f"Game On, {free_chairs} free chairs left")
