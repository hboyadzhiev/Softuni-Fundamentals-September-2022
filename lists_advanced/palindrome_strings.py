words = input().split(" ")
palindrome = input()

def palindr(some_word):
    if some_word == some_word[::-1]:
        return some_word

found_palindromes = [word for word in words if palindr(word)]
palindrome_counter = found_palindromes.count(palindrome)

print(found_palindromes)
print(f"Found palindrome {palindrome_counter} times")

