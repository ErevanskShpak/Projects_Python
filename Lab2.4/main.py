def input_number(phrase):
    while True:
        try:
            number = input(phrase)
            number = int(number)
            break
        except ValueError:
            print("Некорректный ввод")
    return number


a = input_number("Введите делимое: ")
b = input_number("Введите делитель: ")
try:
    print("Результат деления: ", a/b)
except ZeroDivisionError:
    print("Деление на ноль")
finally:
    print("Программа завершена")
