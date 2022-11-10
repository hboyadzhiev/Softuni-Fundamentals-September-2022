students = {}

while True:
    command = input().split(":")
    if len(command) < 2:
        searched_command = command[0].replace("_", " ")
        break
    else:
        name, id, course = command[0], command[1], command[2]
        if course not in students.keys():
            students[course] = {}
        students[course][id] = name

for key, value in students.items():
    if key == searched_command:
        for identity, student_name in value.items():
            print(f"{student_name} - {identity}")
