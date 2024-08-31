import random


def input_number(phrase):
    while True:
        try:
            number = input(phrase)
            number = int(number)
            break
        except ValueError:
            print("Некорректный ввод")
    return number


def create_matrices():
    matrices = [[random.randint(-5, 10) for el1 in range(m)] for el2 in range(n)]

    return matrices


def find_sum(matrices):
    summa = 0
    temp = 0
    for j in range(m):
        for i in range(n):
            if matrices[i][j] < 0:
                temp = 0
                break
            temp += matrices[i][j]

        summa += temp
        temp = 0

    return summa


n = input_number("Введите количество строк матрицы: ")
m = input_number("Введите количество столбцов матрицы: ")

matrices_main = create_matrices()
for el in matrices_main:
    print(el)

summa_main = find_sum(matrices_main)
print("Сумма эл-ов в столбцах без отрицательных: ", summa_main)
