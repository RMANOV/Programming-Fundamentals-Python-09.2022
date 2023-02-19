# Най-добър играч 
# Пепи иска да напишете програма, чрез която да разбере кой е най-добрият играч от световното първенство. 
# Информацията, която получавате ще бъде играч и колко гола е отбелязал. 
# От вас се иска да отпечатате кой е играчът с най-много голове и дали е направил хет-трик. 
# Хет-трик е, когато футболистът е вкарал 3 или повече гола. Ако футболист е вкарал 10 или повече гола, програмата трябва да спре.
# Вход
# От конзолата се четат по два реда до въвеждане на команда "END":
# •	Име на играч – текст
# •	Брой вкарани голове  – цяло положително число в интервала [1 … 10000]
# Изход
# На конзолата да се отпечатат 2 реда :
# •	На първия ред:
#      	"{име на играч} is the best player!"
# •	На втория ред :
# o	 Ако най-добрият футболист е направил хет-трик:
#          	"He has scored {брой голове} goals and made a hat-trick !!!"
# o	Ако най-добрият футболист НЕ е направил хет-трик:
#                    	"He has scored {брой голове} goals."

max_goals = 0
best_player = ""

while True:
    name = input()
    if name == "END":
        break
    goals = int(input())
    if goals >= 10:
        print(f"{name} is the best player!")
        print(f"He has scored {goals} goals and made a hat-trick !!!")
        exit()
    elif goals > max_goals:
        max_goals = goals
        best_player = name

print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")

