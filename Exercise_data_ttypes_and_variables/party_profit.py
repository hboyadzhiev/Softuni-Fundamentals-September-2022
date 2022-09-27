companions_count = int(input())
days = int(input())
coins = 0

if True:
    coins += 50 * days
for day in range(1, days + 1):
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5
        coins -= companions_count * 2
    coins -= companions_count * 2
    if day % 3 == 0:
        coins -= companions_count * 3
    if day % 5 == 0:
        coins += 20 * companions_count


coins_per_companion = int(coins / companions_count)
print(f"{companions_count} companions received {coins_per_companion} coins each.")