def sum_numbers(one, two):
    sum = one + two
    return sum

def subtract(sum, inp3):
    sub = sum - inp3
    return sub

def add_and_subtract(inp1, inp2, inp3):
    current_sum = sum_numbers(inp1, inp2)
    result = subtract(current_sum, inp3)
    return result

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))
