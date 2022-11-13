registered_students = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break
    course_name = command[0]
    student_name = command[1]
    if course_name not in registered_students.keys():
        registered_students[course_name] = []
    registered_students[course_name].append(student_name)

for key, value in registered_students.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")




    
