def total_order_price(product, quantity):
    if product == "coffee":
        price_per_one = 1.50
    elif product == "coke":
        price_per_one = 1.40
    elif product == "water":
        price_per_one = 1.00
    elif product == "snacks":
        price_per_one = 2.00
    result = quantity * price_per_one
    return result

current_product = input()
current_quantity = int(input())
print(f"{total_order_price(current_product, current_quantity):.2f}")

