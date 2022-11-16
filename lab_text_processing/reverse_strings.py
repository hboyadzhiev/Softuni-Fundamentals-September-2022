while True:
    word = input()
    if word == "end":
        break
    reversed = word[::-1]
    print(f"{word} = {reversed}")

