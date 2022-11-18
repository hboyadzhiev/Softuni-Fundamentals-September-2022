# Exercise: You will be given a number. Print the largest number that can be formed from the
# digits of the given number.

number = int(input())
highest = "".join(sorted(str(number), reverse = True))
print(highest)
