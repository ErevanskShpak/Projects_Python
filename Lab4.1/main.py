class String:
    def __init__(self, param=""):
        self.string = param

    def length(self):
        number = 0
        for el in self.string:
            number += 1
        return number

    def add(self, param):
        return self.string + param

    def get(self, i):
        return self.string[i]

    def reverse(self):
        temp = ""
        for el in reversed(self.string):
            temp += el
        return temp

    def get_upper(self):
        temp = ""
        for el in self.string:
            if el.islower():
                temp += el.upper()
        return temp

    def __str__(self):
        return self.string


test = String("экскаватор")
print("Строка: ", test)
print("Метод длины: ", test.length())
print("Метод получения индекса: ", test.get(3))
print("Метод сложения строк: ", test.add(" крут"))
print("Метод реверса строк: ", test.reverse())
print("Метод возведения в верхний регистр: ", test.get_upper())
