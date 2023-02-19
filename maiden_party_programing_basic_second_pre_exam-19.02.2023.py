# Моминско парти
# Михаела държи сама да организира и заплати моминското си парти. 
# Тя планува плащането да стане с приходите от онлайн магазина й. 
# Да се напише програма, която пресмята печалбата от продажбите й.
# Цени на различните артикули:
# •	Любовно послание - 0.60 лв.
# •	Восъчна роза - 7.20 лв.
# •	Ключодържател - 3.60 лв.
# •	Карикатура - 18.20 лв.
# •	Късмет изненада - 22 лв.
# Ако поръчаните артикули са 25 или повече магазинът прави отстъпка 35% от общата цена. 
# От спечелените пари Михаела трябва да предвиди и 10% разход за хостинг. 
# Да се пресметне дали парите ще й стигнат да си плати моминското парти.
# Вход
# От конзолата се четат 6 реда:
# 1.	Цена на моминското парти - реално число в интервала [1.00 … 10000.00]
# 2.	Брой любовни послания - цяло число в интервала [0… 1000]
# 3.	Брой восъчни рози - цяло число в интервала [0 … 1000]
# 4.	Брой ключодържатели - цяло число в интервала [0 … 1000]
# 5.	Брой карикатури - цяло число в интервала [0 … 1000]
# 6.	Брой късмети изненада - цяло число в интервала [0 … 1000]
# Изход
# На конзолата се отпечатва:
# •	Ако парите са достатъчни се отпечатва:
# o	"Yes! {оставащите пари} lv left."
# •	Ако парите НЕ са достатъчни се отпечатва:
# o	"Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

price_party = float(input())
love_letters_count = int(input())
roses_count = int(input())
keysholders_count = int(input())
cariqatures_count = int(input())
surprises_count = int(input())

LOVE_LETTER_PRICE = 0.60
ROSES_PRICE = 7.20
KEYS_PRICE = 3.60
CARIQATURE_PRICE = 18.20
SURPRISE_PRICE = 22.00
HOSTING_PERCENT = 0.10
DISCOUNT = 0.35

total_count = love_letters_count + roses_count + keysholders_count + cariqatures_count + surprises_count
income = 0


if total_count >= 25:
    discount = 0.35
    income = (love_letters_count * LOVE_LETTER_PRICE + roses_count * ROSES_PRICE + keysholders_count * KEYS_PRICE + cariqatures_count * CARIQATURE_PRICE + surprises_count * SURPRISE_PRICE) * (1 - discount)
else:
    income = love_letters_count * LOVE_LETTER_PRICE + roses_count * ROSES_PRICE + keysholders_count * KEYS_PRICE + cariqatures_count * CARIQATURE_PRICE + surprises_count * SURPRISE_PRICE
income = income - income * 0.10 # hosting


difference_income_party = income - price_party

print(f"Yes! {difference_income_party:.2f} lv left." if difference_income_party >= 0 else f"Not enough money! {abs(difference_income_party):.2f} lv needed.")
