# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if 0 < month < 13:
    if month in (1, 3, 5, 7, 8, 10, 12):
        print('в этом месяце', 31, 'день')
    elif month in (4, 6, 9, 11):
        print('в этом месяце', 30, 'дней')
    elif month == 2:
        print('в этом месяце', 28, 'дней')
else:
    print('Вы ввели некорректное число. Введите число от 1 до 12.')