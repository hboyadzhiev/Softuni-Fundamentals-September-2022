items_list = input().split("|")
budget = int(input())
train_ticket = 150
bought_items = []
increased_prices_list = []
total_items_increased_price = 0
total_bought_items_price = 0
enough_budget = False
profit = 0


for item in range(len(items_list)):
    splitted_item = items_list[item].split("->")
    if splitted_item[0] == "Clothes":
        if float(splitted_item[1]) <= 50 and budget >= float(splitted_item[1]):
            budget -= float(splitted_item[1])
            total_bought_items_price += float(splitted_item[1])
            bought_items.append(splitted_item[1])
        else:
            continue
    elif splitted_item[0] == "Shoes":
        if float(splitted_item[1]) <= 35 and budget >= float(splitted_item[1]):
            budget -= float(splitted_item[1])
            total_bought_items_price += float(splitted_item[1])
            bought_items.append(splitted_item[1])
        else:
            continue
    elif splitted_item[0] == "Accessories":
        if float(splitted_item[1]) <= 20.50 and budget >= float(splitted_item[1]):
            budget -= float(splitted_item[1])
            total_bought_items_price += float(splitted_item[1])
            bought_items.append(splitted_item[1])
        else:
            continue

for increased_item_index in range(len(bought_items)):
    increased_prices_list.append(float(bought_items[increased_item_index]) * 1.40)
    total_items_increased_price += float(bought_items[increased_item_index]) * 1.40

profit = total_items_increased_price - total_bought_items_price
if total_items_increased_price + budget >= train_ticket:
    enough_budget = True

for price_index in range(len(increased_prices_list)):
    print(f"{float(increased_prices_list[price_index]):.2f}", end = " ")
print("")
print(f"Profit: {profit:.2f}")
if enough_budget:
    print("Hello, France!")
else:
    print("Not enough money.")