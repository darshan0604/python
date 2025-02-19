class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def get_model(self):
        # self.model = model
        return self.model
    
    def full_name(self):
        return self.brand + " " + self.model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)    
        self.model = model
        self.battery_size = battery_size
    
my_tesla = ElectricCar("Tesla", "Truck ", "87KWH")
print(my_tesla.get_model())
    
    
# my_car = Car("Toyota", "Corolla")
