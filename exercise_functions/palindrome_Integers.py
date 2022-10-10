def palindrome_check(numbers):
        if numbers == numbers[::-1]:
            return True
        else:
            return False

numbers_list = list(map(str, input().split(", ")))
for number in numbers_list:
    print(palindrome_check(number))
