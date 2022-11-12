registered = {}

iterations_count = int(input())

for user in range(iterations_count):
    command = input().split(" ")
    if command[0] == "register":
        username = command[1]
        plate = command[2]
        if username not in registered:
            registered[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered[username]}")

    elif command[0] == "unregister":
        username = command[1]
        if username in registered:
            del registered[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for key, value in registered.items():
    print(f"{key} => {value}")
