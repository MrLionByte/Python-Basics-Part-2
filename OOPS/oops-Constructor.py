# Exercise 1: Simple Class
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi i'm {self.name} and my age is {self.age}"

person = Person("david",26)
print(person.introduce())

# Exercise 3: Constructor Overloading

class Car:
    def __init__(self,make,model,year = 2024) -> None:
        self.make = make
        self.model = model
        self.year = year

        print(self,make, self.model, self.year)

car = Car("Toyota","Skoda",2020)
    