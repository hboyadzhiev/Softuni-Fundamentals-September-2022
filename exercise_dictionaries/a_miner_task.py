resources = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in resources.keys():
        resources[resource] = 0
    resources[resource] += quantity

for material, how_much in resources.items():
    print(f"{material} -> {how_much}")

