def even(number):
    if number % 2 == 0:
        return number

numbers = list(map(int, input().split(", ")))
result = [num for num in range(len(numbers)) if even(numbers[num])]
print(result)

