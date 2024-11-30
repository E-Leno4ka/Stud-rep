from Class.Car import Car

class Truck(Car):
    def __init__(self, model, year, engin_vol, price, mileage, wheel_num):
        super().__init__(model, year, engin_vol, price, mileage, wheel_num)

    def description(self):
        description=(f"Грузовик модели {self.model}, год выпуска {self.year}, объём двигателя {self.engin_vol} л,"
                     f"цена {self.price} тыс.рублей, пробег {self.mileage} км, количество колёс {self.wheel_num}")
        return description
