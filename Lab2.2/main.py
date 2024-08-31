def input_number(phrase, left, right):
    while True:
        try:
            number = input(phrase)
            number = int(number)
            if number < left or number > right:
                raise ValueError
            break
        except ValueError:
            print("Некорректный ввод")

    return number


def lists(arg):
    summa = 0
    for el in arg:
        if el == 0:
            arg.remove(el)

    for el in arg:
        if el % 2 == 0:
            summa += el

    return arg, summa


def sets(arg):
    arg.remove(max(arg))

    return arg


def numbers(arg):
    if arg <= 0:
        return False

    for i in range(2, int(arg**0.5)):
        if arg % i == 0:
            return False

    return True


def string(arg):
    ans = '0'
    big = 0
    for el in arg:
        temp = arg.count(el)
        if temp > big:
            big = temp
            ans = el

    return ans


def func(arg):
    if isinstance(arg, list):
        arg, summa = lists(arg)
        print("Список без 0: ", arg)
        print("Сумма четных: ", summa)

    elif isinstance(arg, set):
        sets(arg)
        print("Множество без макс элемента: ", arg)

    elif isinstance(arg, int):
        if numbers(arg):
            print("Число является простым")
        else:
            print("Число не является простым")

    elif isinstance(arg, str):
        print("Наиболее часто встречающийся символ: ", string(arg))


print("Что вы хотите ввести? ")
print("1. Список")
print("2. Множество")
print("3. Число")
print("4. Строку")
point = input_number("Введите номер: ", 1, 4)

arg_main = ""
match point:
    case 1:
        temp = []
        size = input_number("Введите кол-во элементов: ", 1, 20)
        for i in range(size):
            a = input_number("Введите элемент списка: ", -1000, 1000)
            temp.append(a)

        arg_main = temp
    case 2:
        temp = []
        size = input_number("Введите кол-во элементов: ", 1, 20)
        for i in range(size):
            a = input_number("Введите элемент множества: ", -1000, 1000)
            temp.append(a)

        arg_main = set(temp)
    case 3:
        arg_main = input_number("Введите число: ", -10000, 10000)
    case 4:
        arg_main = input("Введите строку: ")

func(arg_main)