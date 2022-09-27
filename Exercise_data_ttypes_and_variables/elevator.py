capacity = int(input())
num_people = int(input())
num_courses = 0

if capacity % num_people == 0:
    num_courses = capacity // num_people
else:
    num_courses = (capacity // num_people) + 1

print(num_courses)