lst = []

for parts in range(3):
    part = input()
    lst.append(part)

lst[0], lst[2] = lst[2], lst[0]
print(lst)
