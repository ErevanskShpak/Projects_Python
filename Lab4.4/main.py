class CarsForSale:
    __client_count = 0

    def __init__(self, name, age):
        CarsForSale.__client_count += 1
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return CarsForSale.__client_count

    @staticmethod
    def show_signboard():
        print("Мы продаем отличные машины!")


CarsForSale.show_signboard()
car = CarsForSale("BMW", 10)
car2 = CarsForSale("Mercedes", 5)
print(dir(car))
print("Кол-во наших машин в данный момент: ", CarsForSale.get_count())
