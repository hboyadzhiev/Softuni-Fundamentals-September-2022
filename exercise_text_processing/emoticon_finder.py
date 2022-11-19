text = input()
emoticons = []

for index in range(len(text)):
    if text[index] == ":":
        emoticons.append(text[index + 1])
for emoticon in emoticons:
    print(f":{emoticon}")



