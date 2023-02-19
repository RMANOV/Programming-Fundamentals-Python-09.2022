# Калкулатор за екскурзии
# Туристическа агенция предлага екскурзии на различни цени, според сезона и броя на хората. 
# Напишете програма, която да изчислява цената, според данните от таблицата:
# 	Пролет (spring)	Лято (summer)	Есен (autumn)	Зима (winter)
# До 5 човека	50.00 лв. на човек	48.50 лв. на човек	60.00 лв. на човек	86.00 лв. на човек
# Над 5 човека	48.00 лв. на човек	45.00 лв. на човек	49.50 лв. на човек	85.00 лв. на човек
# В зависимост от сезона, може да има отстъпка или оскъпяване на цената, съответно:
# •	При "summer" -> 15% отстъпка
# •	При "winter" -> 8% оскъпяване
# Вход:
# 1.	Първи ред – брой хора – цяло число в интервала [1 … 20]
# 2.	Втори ред – сезон – текст с възможности - "spring", "summer", "autumn" или "winter" 
# Изход:
#    На конзолата се отпечатва 1 ред:
#  •   Цената за екскурзията, форматирана до втория знак след десетичния разделител, в следния формат: "{цената} leva."

number_of_people = int(input())
season = input()
price = 0
total = 0

if season == "spring" and number_of_people <= 5:
    total = number_of_people * 50
elif season == "spring" and number_of_people > 5:
    total = number_of_people * 48
elif season == "summer" and number_of_people <= 5:
    total = number_of_people * 48.50
    total = total - (total * 0.15)
elif season == "summer" and number_of_people > 5:
    total = number_of_people * 45
    total = total - (total * 0.15)
elif season == "autumn" and number_of_people <= 5:
    total = number_of_people * 60
elif season == "autumn" and number_of_people > 5:
    total = number_of_people * 49.50
elif season == "winter" and number_of_people <= 5:
    total = number_of_people * 86
    total = total + (total * 0.08)
elif season == "winter" and number_of_people > 5:
    total = number_of_people * 85
    total = total + (total * 0.08)

print(f"{total:.2f} leva.")