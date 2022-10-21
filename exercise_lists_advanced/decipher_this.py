message = [word for word in input().split(" ")]

def num_to_letter(symbols):
    digits = [x for x in symbols if x.isdigit()]
    list_to_string = ''.join(digits)
    letter = chr(int(list_to_string))
    return letter
def letter_switch(some_word):
    if len(some_word) > 1:
        switched_word = some_word[-1::] + some_word[1:-1] + some_word[0]
    else:
        switched_word = some_word
    return switched_word
def word_without_digits(the_word):
    new_wordd = the_word[len(str(ord(num_to_letter(the_word))))::]
    return new_wordd

new_words_list = [num_to_letter(new_word) + letter_switch(word_without_digits(new_word)) for new_word in message]
print(' '.join(new_words_list))
