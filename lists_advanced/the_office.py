happiness_list = input().split(" ")
improvement_factor = int(input())

multiplied = list(map(lambda x: int(x) * improvement_factor, happiness_list))
filtered_happy = list(filter(lambda y: y >= sum(multiplied) / len(multiplied), multiplied))

if len(filtered_happy) >= len(multiplied) /2:
    print(f"Score: {len(filtered_happy)}/{len(multiplied)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happy)}/{len(multiplied)}. Employees are not happy!")
