def input_number(phrase):
    while True:
        try:
            number = input(phrase)
            number = float(number)
            break
        except ValueError:
            print("Некорректный ввод")
    return number


def input_operation():
    while True:
        try:
            operation = input("Введите операцию: ")
            if operation != '0' and operation != '+' and operation != '-' and operation != '/' and operation != '*':
                raise ValueError
            break
        except ValueError:
            print("Некорректный ввод")
    return operation


while True:
    operation = input_operation()
    if operation == '0':
        break
    number1 = input_number("Введите первое число: ")

    number2 = input_number("Введите второе число: ")

    match operation:
        case '+':
            print("Результат: ", number1 + number2)
        case '-':
            print("Результат: ", number1 - number2)
        case '*':
            print("Результат: ", number1 * number2)
        case '/':
            try:
                print("Результат: ", number1 / number2)
            except ZeroDivisionError:
                print("Деление на ноль!")
