input_number = input("Введите натуральное число: ")
while not input_number.isdigit() or int(input_number) <= 0:
    input_number = input("Некорректный ввод, введите натуральное число: ")
input_number = int(input_number)

sum_of_digits = 0
while input_number:
    if (input_number % 2) == 0:
        sum_of_digits += input_number % 10
    input_number //= 10

print("Сумма четных цифр= ", sum_of_digits)
