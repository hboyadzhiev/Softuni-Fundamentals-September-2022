def enough_quantity(food, hay, cover, pig):
    not_enough = False
    for day in range(1, 31):
        food -= 0.3
        if food <= 0:
            not_enough = True
            break
        if day % 2 == 0:
            hay -= (food * 0.05)
            if hay <= 0:
                not_enough = True
                break
        if day % 3 == 0:
            cover -= (pig / 3)
            if cover <= 0:
                not_enough = True
                break
    if not_enough:
        return "Merry must go to the pet store!"
    else:
        return f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}."


food_quanitty_kgs = float(input())
hay_quanitty_kgs = float(input())
cover_quanitty_kgs = float(input())
pig_weight_kgs = float(input())

print(enough_quantity(food_quanitty_kgs, hay_quanitty_kgs, cover_quanitty_kgs, pig_weight_kgs))