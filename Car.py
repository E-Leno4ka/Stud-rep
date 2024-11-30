class Car:
    def __init__(self, model, year, engin_vol, price, mileage, wheel_num):
        self.model=model
        self.year=year
        self.engin_vol=engin_vol
        self.price=price
        self.mileage=mileage
        self.wheel_num=wheel_num
        print('Создан новый автомобиль')

    def description(self):
        description=(f"Автомобиль модели {self.model}, год выпуска {self.year}, объём двигателя {self.engin_vol} л,"
                     f"цена {self.price} тыс.рублей, пробег {self.mileage} км, количество колёс {self.wheel_num}")
        return description
