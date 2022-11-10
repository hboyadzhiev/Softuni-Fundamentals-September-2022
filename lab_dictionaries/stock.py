products = input().split(" ")
products_dictionary = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    products_dictionary[key] = value

searched_products = input().split(" ")
for product in searched_products:
    if product in products_dictionary:
        print(f"We have {products_dictionary[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
