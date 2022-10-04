listt = input().split("#")
water = int(input())
effort = 0
total_fire = 0
putted_out_cells = []


for cell in range(len(listt)):
    splitted_cell = listt[cell].split(" = ")
    if splitted_cell[0] == "High":
        if 81 <= int(splitted_cell[1]) <= 125 and water >= int(splitted_cell[1]):
            water -= int(splitted_cell[1])
            total_fire += int(splitted_cell[1])
            effort += int(splitted_cell[1]) * 0.25
            putted_out_cells.append(splitted_cell[1])
        else:
            continue
    elif splitted_cell[0] == "Medium":
        if 51 <= int(splitted_cell[1]) <= 80 and water >= int(splitted_cell[1]):
            water -= int(splitted_cell[1])
            total_fire += int(splitted_cell[1])
            effort += int(splitted_cell[1]) * 0.25
            putted_out_cells.append(splitted_cell[1])
        else:
            continue
    elif splitted_cell[0] == "Low":
        if 1 <= int(splitted_cell[1]) <= 50 and water >= int(splitted_cell[1]):
            water -= int(splitted_cell[1])
            total_fire += int(splitted_cell[1])
            effort += int(splitted_cell[1]) * 0.25
            putted_out_cells.append(splitted_cell[1])
        else:
            continue
print("Cells:")
for cell_index in range(len(putted_out_cells)):
    print(f" - {putted_out_cells[cell_index]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


