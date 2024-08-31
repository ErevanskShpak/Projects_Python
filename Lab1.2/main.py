input_string = input("Введите строку: ")
words = input_string.split(" ")

print("Самое длинное слово: ", max(words, key=len))
print("Реверсивная строка: ", input_string.swapcase())

sum_of_digits = 0
for i in input_string:
    if i.isdigit():
        sum_of_digits += 1

print("Количество цифр в строке: ", sum_of_digits)
