numbers_list = [(x) for x in input().split(", ")]
positive = [num for num in numbers_list if int(num) >= 0]
negative = [num for num in numbers_list if int(num) < 0]
even = [num for num in numbers_list if int(num) % 2 == 0]
odd = [num for num in numbers_list if int(num) % 2 != 0]

positive_string = ", ".join(positive)
negative_string = ", ".join(negative)
even_string = ", ".join(even)
odd_string = ", ".join(odd)

print(f"Positive: {(positive_string)}")
print(f"Negative: {negative_string}")
print(f"Even: {even_string}")
print(f"Odd: {odd_string}")
