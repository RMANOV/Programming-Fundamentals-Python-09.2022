# Смени
# Любимият отбор на Пепи е на финал, но започва да губи мача. Треньорът на отбора не знае какви смени да направи, за да обърне резултата. 
# Напишете програма, с която ще разберете кой са първите 6 валидни смени, които могат да се направят.  
# Знаем, че всяка цифра от двата номера е в даден интервал:
# •	Първата цифра на първото число е в интервала от цифрата K до 8, включително.
# •	Втората цифра на първото число е в интервала от 9 до L, включително.
# •	Първата цифра на второто число е в интервала от цифрата M до 8, включително.
# •	Втората цифра на второто число е в интервала от 9 до N, включително.
# За да бъде възможна една смяна, първата цифра на всеки от номерата трябва да бъде четна, а втората -  нечетна.
# За да бъде валидна една смяна, то номерата НЕ трябва да съвпадат.
# Вход:
# От конзолата се четат 4 реда:
# •	K – цяло число в интервала [0..8]
# •	L – цяло число в интервала [0..9]
# •	M– цяло число в интервала [0..8]
# •	N – цяло число в интервала [0..9]
# Изход:
# На конзолата да се отпечатат първите 6 валидни смени по следния начин:
# •	Ако смяната е възможна и номерата НЕ съвпадат, тя Е валидна и трябва да се отпечата:
# "{K}{L} - {M}{N}"
# •	Ако смяната е възможна, но номерата съвпадат, тя НЕ е валидна и трябва да се отпечата:
# "Cannot change the same player."

def is_valid_change(k, l, m, n):
    if k % 2 == 0 and l % 2 != 0 and m % 2 == 0 and n % 2 != 0:
        if k != m or l != n:
            return True
    return False


def print_valid_change(k, l, m, n):
    if is_valid_change(k, l, m, n):
        print(f"{k}{l} - {m}{n}")
    else:
        print("Cannot change the same player.")


def change_players(k, l, m, n):
    valid_changes = []
    for i in range(k, 9):
        for j in range(9, l, -1):
            for x in range(m, 9):
                for y in range(9, n, -1):
                    if is_valid_change(i, j, x, y):
                        valid_changes.append(f"{i}{j} - {x}{y}")
                        if len(valid_changes) == 6:
                            break
                if len(valid_changes) == 6:
                    break
            if len(valid_changes) == 6:
                break
        if len(valid_changes) == 6:
            break
    return valid_changes


def main():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    
    valid_changes = change_players(k, l, m, n)
    
    print_valid_change(k, l, m, n)
    for change in valid_changes:
        print(change)


if __name__ == "__main__":
    main()
