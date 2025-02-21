class Car:
    total_cars = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars = Car.total_cars + 1
        
    def get_model(self):
        return self.model
    
    def full_name(self):
        return f"{self.brand}  {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)    
        self.model = model
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
my_tesla = ElectricCar("Tesla", "Truck ", "87KWH")
print(my_tesla.get_model())

print(my_tesla.fuel_type())
    
safari = Car("Tata", "Safari")
print(safari.fuel_type())
safarithree = Car("Tata", "Safari")
print(safarithree.fuel_type())

print(Car.total_cars)
