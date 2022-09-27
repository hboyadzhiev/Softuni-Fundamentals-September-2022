lines_count = int(input())

sum = 0

for lines in range(lines_count):
    line = input()
    sum += ord(line)

print(f"The sum equals: {sum}")

