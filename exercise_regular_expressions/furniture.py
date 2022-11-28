import re

total_spent = 0
names = []
pattern = r"\>>([A-Za-z]+)\<<([0-9]+(\.[0-9]+)?)\!([0-9]+)"

while True:
    command = input()
    if command == "Purchase":
        break
    matches = re.search(pattern, command)
    if matches:
        name, price, decimal, quantity = matches.groups()
        names.append(name)
        current_sum_spent = int(quantity) * float(price)
        total_spent += current_sum_spent

print("Bought furniture:")
for purchase in names:
    print(purchase)
print(f"Total money spend: {total_spent:.2f}")

