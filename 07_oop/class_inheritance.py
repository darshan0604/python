# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"


class Cat(Animal):
    def meow(self):
        return f"{self.name} says meow!;"


# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog2.eat())  # Buddy is eating
print(my_dog2.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())  # Buddy says woof!

my_cat = Cat("Ketny")
print(my_cat.sleep())  # Ketny is sleeping
print(my_cat.meow())  # Ketny says meow!
