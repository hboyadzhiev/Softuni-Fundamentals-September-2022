lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets = lost_fights_count // 2
swords = lost_fights_count // 3
shields = lost_fights_count // 6
armors = lost_fights_count // 12

expenses = (helmets * helmet_price) + (swords * sword_price) + (shields * shield_price) + (armors * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")