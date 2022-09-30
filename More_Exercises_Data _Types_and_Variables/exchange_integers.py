a = int(input())
b = int(input())

new_line = "/n"

print(f"Before:")
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a


print("After:")
print(f"a = {a}")
print(f"b = {b}")
