number = int(input())
synonyms_dict = {}

for inpt in range(number):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)

for word in synonyms_dict:
    print(f"{word} - {', '.join(synonyms_dict[word])}")



