numbers = [int(i) for i in input().split()]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))