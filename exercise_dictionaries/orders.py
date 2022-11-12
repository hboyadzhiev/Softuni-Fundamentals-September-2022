orders = {}

while True:
    line = input()
    if line == "buy":
        break
    splitted_ilne = line.split(" ")
    name = splitted_ilne[0]
    price = float(splitted_ilne[1])
    quantity = int(splitted_ilne[2])

    if name not in orders.keys():
        orders[name] = []
        orders[name].append(price)
        orders[name].append(quantity)
    else:
        orders[name][1] += quantity
    if price != orders[name][0]:
        orders[name][0] = price

for key, value in orders.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")

