input_number = input("Введите натуральное число: ")
while not input_number.isdigit() or int(input_number) <= 0:
    input_number = input("Некорректный ввод, введите натуральное число: ")
input_number = int(input_number)

result_list = [1]
for it in range(2, input_number // 2 + 1):
    if input_number % it == 0:
        result_list.append(it)
result_list.append(input_number)

print("Все делители введенного числа: ", result_list)
print("Минимальный делитель: ", 1)
print("Максимальный делитель: ", input_number)
