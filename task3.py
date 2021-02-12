month = int(input("Введите целое число от 1  до 12 - это будет месяц года  : "))
year = ("январь февраль март апрель май июнь июль август сентябрь октябрь ноябрь декабрь").split()

seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
if (month >12) or (month < 1):
    print("Нет такого месяца")
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

idx = month%12
i = idx//3
year_season = ['Зима','весна','лето','осень']
print("Сезон года - ", year_season[i])