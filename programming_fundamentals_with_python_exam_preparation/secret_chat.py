message = input()

do_not_print = False

while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {message}")
        break
    else:
        splitted = command.split(":|:")
        action = splitted[0]
        if action == "InsertSpace":
            index = int(splitted[1])
            message = message[:index] + " " + message[index:]
        elif action == "Reverse":
            substring = splitted[1]
            if substring in message:
                message = message.replace(substring, "", 1)
                message = message + substring[::-1]
            else:
                print("error")
                do_not_print = True
        elif action == "ChangeAll":
            substring = splitted[1]
            replacement = splitted[2]
            message = message.replace(substring, replacement)
    if do_not_print == False:
        print(message)
    do_not_print = False
