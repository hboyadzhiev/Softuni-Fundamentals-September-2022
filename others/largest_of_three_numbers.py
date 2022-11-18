# A program that receives three whole numbers and prints the largest one.

first_num = int(input())
second_num = int(input())
third_num = int(input())

if first_num > second_num and first_num > third_num:
 print(first_num)
elif second_num > first_num and second_num > third_num:
 print(second_num)
else:
 print(third_num)


# 2nd solution:

number = int(input())
largest_num = number

for num in range(2):
    number = int(input())
    if number > largest_num:
        largest_num = number

print(largest_num)