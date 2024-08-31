class Animal:
    def __init__(self, breed, price, who):
        self.__breed = breed
        self.__price = price
        self.__who = who

    @staticmethod
    def how_move():
        print("Я передвигаюсь по-разному")

    def __str__(self):
        return f"{self.__who}\t{self.__breed}\t{self.__price}"

    def get_price(self):
        return self.__price


class Fish(Animal):
    @staticmethod
    def how_move():
        print("Я плаваю")


class Bird(Animal):
    @staticmethod
    def how_move():
        print("Я летаю")


class PetShop:
    def __init__(self):
        self.__animals = []

    def push(self, param):
        self.__animals.append(param)

    def __str__(self):
        temp = ""
        for el in self.__animals:
            temp += str(el)
            temp += "\n"
        return temp

    def __getitem__(self, item):
        return self.__animals[item]


store = PetShop()

f = open("petshop.txt", 'r', encoding='utf-8')
for line in f:
    content = line.split()
    if content[0] == "Рыба":
        store.push(Fish(content[1], content[2], content[0]))
    else:
        store.push(Bird(content[1], content[2], content[0]))
f.close()

print(store)

maxi = store[0]
for el in store:
    if int(el.get_price()) > int(maxi.get_price()):
        maxi = el
print(f"Самая дорогая порода: {maxi}")

f = open("result.txt", 'w', encoding='utf-8')
f.write(f"Самая дорогая порода: {maxi}")
f.close()
