number_of_snowballs = int(input())
weight = 0
time_needed = 0
quality = 0
best_value = 0

for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_of_snowball = int(input())
    quality_of_snowball = int(input())
    current_value = (weight_of_snowball / time_of_snowball) ** quality_of_snowball
    if current_value > best_value:
        weight = weight_of_snowball
        time_needed = time_of_snowball
        quality = quality_of_snowball
        best_value = current_value

print(f"{weight} : {time_needed} = {int(best_value)} ({quality})")