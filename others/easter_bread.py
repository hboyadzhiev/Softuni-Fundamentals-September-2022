
#  Exercise: Since it is Easter, you have decided to make some loaves of Easter bread
#  and exchange them for eggs. Create a program that calculates how many loaves you can make
#  (according to the recipe) with the budget you have. Here is the recipe for one loaf:
#  Eggs 1 pack Flour 1 kg Milk 0.250 l First, you will receive your budget.
#  Then, you will receive the price for 1 kg flour. The price for 1 pack of eggs
#  is 75% of the price for 1 kg flour. The price for 1L milk is 25% more than the price for 1 kg flour.
#  Keep in mind that you use only 250ml milk for a bread. Start cooking the loaves and keep making
#  them until you have enough budget. Keep in mind that: · For every loaf of bread that you make,
#  you will receive 3 colored eggs. · For every 3rd bread you make, you will
#  lose some of your colored eggs after receiving the usual 3 colored eggs for your bread.
#  The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves
#  - ({current_bread_count} - 2)

budget = float(input())
price_per_kg_flour = float(input())

price_for_pack_eggs = 0.75 * price_per_kg_flour
milk_price = (1.25 * price_per_kg_flour) / 4
price_loaf_bread = price_per_kg_flour + price_for_pack_eggs + milk_price
remaining_budget = budget
loaves_counter = 0
eggs_counter = 0

while remaining_budget >= price_loaf_bread:
    loaves_counter += 1
    eggs_counter += 3
    if loaves_counter % 3 == 0:
        eggs_counter -= (loaves_counter - 2)

    remaining_budget -= price_loaf_bread

print(
    f"You made {loaves_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {remaining_budget:.2f}BGN left.")