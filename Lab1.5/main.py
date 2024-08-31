my_dict = {"Плюшевый мишка": ["Мех", 60, 10],
           "Конструктор LEGO: Дом": ["Пластмасса", 200, 5],
           "Кукла Barbie": ["Пластмасса, ткань", 50, 20],
           "Коллекционная машинка": ["Пластмасса", 100, 5]}

print("Магазин игрушек")

menu = 1
while menu:
    print("\nМеню")
    print("1. Просмотр состава игрушек;")
    print("2. Просмотр цены игрушек;")
    print("3. Просмотр количества игрушек;")
    print("4. Просмотр всей информации об игрушках;")
    print("5. Покупка;")
    print("6. До свидания.")

    input_menu = input("Введите пункт меню: ")
    while not input_menu.isdigit() or int(input_menu) < 1 or int(input_menu) > 6:
        input_menu = input("Некорректный ввод, пункт меню должен быть цифрой от 1 до 6: ")

    match input_menu:
        case "1":
            print(f"\n{'Название':<25} {'Состав'}\n")
            for key in my_dict:
                print(f"{key:<25} {my_dict[key][0]}")

        case "2":
            print(f"\n{'Название':<25} {'Цена'}\n")
            for key in my_dict:
                print(f"{key:<25} {my_dict[key][1]}")

        case "3":
            print(f"\n{'Название':<25} {'Количество'}\n")
            for key in my_dict:
                print(f"{key:<25} {my_dict[key][2]}")

        case "4":
            print(f"\n{'Название':<25} {'Состав':<20} {'Цена':<10} {'Количество'}\n")
            for key in my_dict:
                print(f"{key:<25} {my_dict[key][0]:<20} {my_dict[key][1]:<10} {my_dict[key][2]}")

        case "5":
            isAlso = 1
            paycheck = 0
            while isAlso:
                input_name = input("Введите название игрушки: ")
                isBe = 1
                while isBe:
                    for key in my_dict:
                        if key == input_name:
                            isBe = 0

                    if isBe:
                        input_name = input("Такой игрушки нет, повторите попытку: ")

                input_number = input("Введите количество игрушек для покупки: ")
                while not input_number.isdigit() or int(input_number) <= 0 or int(input_number) > my_dict[input_name][2]:
                    input_number = input("Ввод некорректен или отсутствует такое количество товара, повторите попытку: ")
                input_number=int(input_number)

                print("Цена выбранных товаров: ", input_number * my_dict[input_name][1])
                paycheck += input_number * my_dict[input_name][1]
                my_dict[input_name][2] -= input_number
                print("Количество оставшихся товаров: ", my_dict[input_name][2])

                isAlso = input("Вы хотите продолжить покупку?\n 1. Да; 0. Нет\nВвод: ")
                while not isAlso.isdigit() or int(isAlso) < 0 or int(isAlso) > 1:
                    isAlso = input("Некорректный ввод, ввод должен быть от 0 до 1: ")
                isAlso = int(isAlso)

            print("\nОбщий чек: ", paycheck)

        case "6":
            menu = 0
