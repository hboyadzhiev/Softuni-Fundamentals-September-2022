def perfect_number(number):
    sum_of_proper_divisors = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_proper_divisors += num
    if sum_of_proper_divisors == number:
        return "We have a perfect number!"
    return "It's not so perfect."

current_number = int(input())
print(perfect_number(current_number))
