days_of_adventure = int(input())
number_of_players = int(input())
groups_energy = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())

out_of_energy = False

overall_food = days_of_adventure * number_of_players * food_per_day_for_one_person
overall_water = days_of_adventure * number_of_players * water_per_day_for_one_person

current_food = overall_food
current_water = overall_water

for day in range(1, days_of_adventure + 1):
    energy_loss = float(input())
    groups_energy -= energy_loss
    if groups_energy <= 0:
        out_of_energy = True
        break
    if day % 2 == 0:
        groups_energy = groups_energy * 1.05
        current_water -= current_water * 0.30
    if day % 3 == 0:
        current_food -= current_food / number_of_players
        groups_energy += groups_energy * 0.10

if out_of_energy:
    print(f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")


