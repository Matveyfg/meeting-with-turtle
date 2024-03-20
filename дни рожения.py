import datetime

month = int(input("Введите месяц рождения (1-12): "))
day = int(input("Введите день рождения (1-31): "))


with open("birthday.txt", "w") as f:
    f.write("Date: %02d.%02d\n" % (month, day))

# Цикл по 20 годам
for year in range(2021, 2041):
    bday = datetime.date(year, month, day)
    day_of_week = bday.strftime("%A")
print(month, day, year, day_of_week)