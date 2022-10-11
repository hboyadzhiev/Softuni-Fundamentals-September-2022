def fact_division(num1, num2):
    factorial1 = 0
    factorial2 = 0
    for number in range(0, num1 + 1):
        factorial1 *= number
        if factorial1 == 0:
            factorial1 += 1
    for number in range(0, num2 + 1):
        factorial2 *= number
        if factorial2 == 0:
            factorial2 += 1
    division = factorial1 / factorial2

    return f"{division:.2f}"

number1 = int(input())
number2 = int(input())
print(fact_division(number1, number2))

