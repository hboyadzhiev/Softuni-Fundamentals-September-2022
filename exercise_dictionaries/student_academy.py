rows_count = int(input())
grades = {}

for grade in range(rows_count):
    student = input()
    grade = float(input())
    if student not in grades.keys():
        grades[student] = []
    grades[student].append(grade)

for key, value in grades.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        print(f"{key} -> {average:.2f}")

