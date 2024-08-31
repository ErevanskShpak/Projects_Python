from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self, states_light):
        if len(states_light) != 3:
            raise ValueError
        temp = list(states_light.keys())
        if (temp[0] != "Красный" or temp[1] != "Желтый"
                or temp[2] != "Зеленый"):
            raise ValueError

        for color, work_time in states_light.items():
            self.__color = color

            print(f"Светофор переключился на {self.__color}", f" на {work_time} секунд")
            sleep(work_time)


states = {"Красный": 7,"Желтый": 2, "Зеленый": 10}
tl = TrafficLight()
print(help(tl))
try:
    tl.running(states)
except ValueError:
    print("Неверный порядок режимов")
