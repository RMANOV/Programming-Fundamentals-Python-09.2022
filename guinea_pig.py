

food = float(input())
hay = float(input())
cover = float(input())
pigs_weight = float(input())


food_in_gr = food * 1000
hay_in_gr = hay * 1000
cover_in_gr = cover * 1000
pigs_weight_in_gr = pigs_weight * 1000


for i in range(1, 31):
    food_in_gr -= 300
    if i % 2 == 0:
        hay_in_gr -= 0.05 * food_in_gr
    if i % 3 == 0:
        cover_in_gr -= pigs_weight_in_gr * 1/3
    if food_in_gr < 0 or hay_in_gr < 0 or cover_in_gr < 0:
        print(f"Merry must go to the pet store!")
        break
    else:
        continue

if food_in_gr >= 0 and hay_in_gr >= 0 and cover_in_gr >= 0:
    food_in_kg = food_in_gr / 1000
    hay_in_kg = hay_in_gr / 1000
    cover_in_kg = cover_in_gr / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_in_kg:.2f}, Hay: {hay_in_kg:.2f}, Cover: {cover_in_kg:.2f}.")
