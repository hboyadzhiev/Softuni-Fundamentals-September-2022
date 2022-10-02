factor = int(input())
count = int(input())
list = []

for num in range(1, count + 1):
    current_number = factor * num
    list.append(current_number)
print(list)