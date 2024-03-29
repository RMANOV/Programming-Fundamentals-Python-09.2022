# Тренировка
# Г-жа Иванова иска да отслабне след празниците. Започвайки тренировка, първия ден тя пробягва М километра. 
# Следващите N дни, тя увеличава дневната си норма с К%. За да успее да отслабне, тя трябва да избяга минимум 1 000 км. 
# Съставете програма, която при получени начални километри, брой дни и проценти, с които тя ще увеличава всеки ден нормата си, 
# ще проверява дали километрите, които тя е избягала са достатъчни. 
# Ако километрите не са достатъчни, на конзолата да се изведат недостигащите километри. 
# Ако са достатъчни да се изведе съобщение в което г-жа Иванова е поздравена за добре свършената работа.
# Вход:
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – N – брой дни, в които г-жа Иванова тренира  – цяло число в интервала [1...50]
# •	На втория ред – M – километрите, които е избягала първия ден – реално число в интервала [1.00…500.00]
# •	За всеки един ден на отделен ред :
# 	Процентите, с които се увеличава дневната си норма – цяло число в интервала [1…100]
# Изход:
# Да се отпечата на конзолата 1 ред, както следва:
# •	Ако пробяганите километри са >= 1 000 км – да се отпечатва съобщение:
# "You've done a great job running {избяганите километри повече от 1000} more   kilometers!"
# •	 Ако пробяганите километри са < 1 000 км – да се отпечата съобщение:
# "Sorry Mrs. Ivanova, you need to run {недостигащите километри} more kilometers"
# Резултатът да се форматира до по-голямото цяло число.

n = int(input())  # Четем броя дни
m = float(input())  # Четем километрите, които е избягала първия ден

total_km = m  # Инициализираме общия брой километри с километрите, които е избягала първия ден

# Обхождаме всички останали дни и увеличаваме нормата на г-жа Иванова
for i in range(n):
    k = int(input())  # Четем процентите, с които се увеличава нормата
    m = m * (1 + k / 100)  # Пресмятаме километрите за текущия ден
    total_km += m  # Добавяме ги към общия брой километри

# Проверяваме дали г-жа Иванова е избягала достатъчно километри
if total_km >= 1000:
    extra_km = int(total_km - 1000)  # Изчисляваме колко километра повече е избягала
    # round() - закръгля до по-голямото цяло число
    extra_km = round(extra_km, 0)
    print(f"You've done a great job running {extra_km+1} more kilometers!")
else:
    needed_km = int(1000 - total_km)  # Изчисляваме колко километра още трябва да избяга
    # round() - закръгля до по-голямото цяло число
    needed_km = round(needed_km, 0)
    print(f"Sorry Mrs. Ivanova, you need to run {needed_km+1} more kilometers")
