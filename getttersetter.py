class Car:
    def __init__(self,brand,model,size):
        self.__brand=brand
        self.model=model
        self._size=size
    
    def set_brand(self,brand):
        self.__brand=brand

    def get_brand(self):
         return self.__brand
    
my_car=Car("Toyota","Camry","100 kwh")
print(my_car.get_brand())
print(my_car.model)
my_car.set_brand("Chake")
print(my_car.get_brand())
