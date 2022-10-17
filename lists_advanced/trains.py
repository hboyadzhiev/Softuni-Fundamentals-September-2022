number_of_wagons = int(input())
train = [0] * number_of_wagons
command = input()

while command != "End":
    token = command.split(" ")
    action = token[0]
    if action == "add":
        train[-1] += int(token[1])
    elif action == "insert":
        train[int(token[1])] += int(token[2])
    elif action == "leave":
        train[int(token[1])] -= int(token[2])
    command = input()
print(train)
