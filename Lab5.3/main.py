import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-5, 12, 1.75)
print("Значения аргумента: ", x)

a = 12.1
y = np.round((np.exp(x * a) - 3.45 * x), 2)
print("Значения функции: ", y)

print("Наибольшее значение функции: ", np.max(y))
print("Наименьшее значение функции: ", np.min(y))
print("Среднее значение функции: ", np.mean(y))
print("Количество значений функции: ", y.size)
print("Отсортированные по убыванию значения функции: ", np.sort(y)[::-1])

plt.plot(x, y, label="y(x)")
plt.hlines(np.mean(y), x[0], x[-1], color="r", label="у avg")
plt.yscale(value="log")

plt.title("Графики функций")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="lower right")
plt.show()
