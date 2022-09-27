lines_number = int(input())
tank_capacity = 255
liters_in_tank = 0

for lines in range(lines_number):
    water_liters = int(input())
    if water_liters > tank_capacity:
        print("Insufficient capacity!")
        continue
    if water_liters <= tank_capacity:
        tank_capacity -= water_liters
        liters_in_tank += water_liters
print(liters_in_tank)



